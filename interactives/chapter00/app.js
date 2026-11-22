(() => {
  const isVi = document.documentElement.lang === "vi";
  const t = (vi, en) => (isVi ? vi : en);
  const plotlyConfig = { displayModeBar: false, responsive: true };

  function byId(id) {
    return document.getElementById(id);
  }

  function num(value) {
    return Number(value);
  }

  function fmt(value, digits = 2) {
    if (!Number.isFinite(value)) {
      return "0";
    }
    return value
      .toFixed(digits)
      .replace(/\.0+$/, "")
      .replace(/(\.\d*[1-9])0+$/, "$1");
  }

  function bindRange(id, formatter) {
    const input = byId(id);
    if (!input) {
      return null;
    }
    const output = byId(`${id}-value`);
    const sync = () => {
      if (output) {
        output.textContent = formatter ? formatter(num(input.value)) : String(input.value);
      }
    };
    input.addEventListener("input", sync);
    input.addEventListener("change", sync);
    sync();
    return input;
  }

  function attachRender(ids, render) {
    ids.forEach((id) => {
      const element = byId(id);
      if (element) {
        element.addEventListener("input", render);
        element.addEventListener("change", render);
      }
    });
    render();
  }

  function linspace(start, end, count) {
    if (count <= 1) {
      return [start];
    }
    const values = [];
    const step = (end - start) / (count - 1);
    for (let i = 0; i < count; i += 1) {
      values.push(start + step * i);
    }
    return values;
  }

  function approxIntegral(fn, a, b, steps = 2000, weightFn = () => 1) {
    const h = (b - a) / steps;
    let total = 0;
    for (let i = 0; i < steps; i += 1) {
      const xLeft = a + i * h;
      const xRight = xLeft + h;
      total += 0.5 * h * (fn(xLeft) * weightFn(xLeft) + fn(xRight) * weightFn(xRight));
    }
    return total;
  }

  function computeIntersections(xs, ys, level) {
    const hits = [];
    for (let i = 0; i < xs.length - 1; i += 1) {
      const y1 = ys[i] - level;
      const y2 = ys[i + 1] - level;
      if (Math.abs(y1) < 1e-8) {
        hits.push(xs[i]);
      }
      if (y1 === 0 || y2 === 0 || y1 * y2 > 0) {
        continue;
      }
      const ratio = y1 / (y1 - y2);
      hits.push(xs[i] + ratio * (xs[i + 1] - xs[i]));
    }
    return hits;
  }

  function baseLayout(extra = {}) {
    return {
      margin: { l: 48, r: 20, t: 18, b: 42 },
      paper_bgcolor: "#ffffff",
      plot_bgcolor: "#ffffff",
      showlegend: true,
      legend: { orientation: "h", y: -0.22, ...(extra.legend || {}) },
      xaxis: {
        gridcolor: "#e5e7eb",
        zeroline: false,
        linecolor: "#cbd5e1",
        mirror: true,
        ...(extra.xaxis || {}),
      },
      yaxis: {
        gridcolor: "#e5e7eb",
        zeroline: false,
        linecolor: "#cbd5e1",
        mirror: true,
        ...(extra.yaxis || {}),
      },
      ...extra,
    };
  }

  function plotIfPresent(id, data, layout) {
    const element = byId(id);
    if (!element || !window.Plotly) {
      return;
    }
    window.Plotly.react(element, data, layout, plotlyConfig);
  }

  function clearCanvas(canvas) {
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    return ctx;
  }

  function makeTransform({
    canvas,
    left = 0,
    top = 0,
    width = canvas.width,
    height = canvas.height,
    xMin,
    xMax,
    yMin,
    yMax,
    padding = 30,
  }) {
    const innerLeft = left + padding;
    const innerRight = left + width - padding;
    const innerBottom = top + height - padding;
    const innerTop = top + padding;
    return {
      left,
      top,
      width,
      height,
      xMin,
      xMax,
      yMin,
      yMax,
      mapX(x) {
        return innerLeft + ((x - xMin) / (xMax - xMin)) * (innerRight - innerLeft);
      },
      mapY(y) {
        return innerBottom - ((y - yMin) / (yMax - yMin)) * (innerBottom - innerTop);
      },
    };
  }

  function drawPanelFrame(ctx, tr, title) {
    ctx.save();
    ctx.fillStyle = "#ffffff";
    ctx.strokeStyle = "#e5e7eb";
    ctx.lineWidth = 1.2;
    ctx.fillRect(tr.left, tr.top, tr.width, tr.height);
    ctx.strokeRect(tr.left, tr.top, tr.width, tr.height);
    if (title) {
      ctx.fillStyle = "#334155";
      ctx.font = "600 14px Inter, sans-serif";
      ctx.fillText(title, tr.left + 14, tr.top + 20);
    }
    ctx.restore();
  }

  function drawGrid(ctx, tr, stepX = 1, stepY = 1, color = "#eef2f7") {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = Math.ceil(tr.xMin / stepX) * stepX; x <= tr.xMax + 1e-8; x += stepX) {
      const px = tr.mapX(x);
      ctx.moveTo(px, tr.mapY(tr.yMin));
      ctx.lineTo(px, tr.mapY(tr.yMax));
    }
    for (let y = Math.ceil(tr.yMin / stepY) * stepY; y <= tr.yMax + 1e-8; y += stepY) {
      const py = tr.mapY(y);
      ctx.moveTo(tr.mapX(tr.xMin), py);
      ctx.lineTo(tr.mapX(tr.xMax), py);
    }
    ctx.stroke();
    ctx.restore();
  }

  function drawAxes(ctx, tr) {
    ctx.save();
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    if (tr.xMin < 0 && tr.xMax > 0) {
      const px = tr.mapX(0);
      ctx.moveTo(px, tr.mapY(tr.yMin));
      ctx.lineTo(px, tr.mapY(tr.yMax));
    }
    if (tr.yMin < 0 && tr.yMax > 0) {
      const py = tr.mapY(0);
      ctx.moveTo(tr.mapX(tr.xMin), py);
      ctx.lineTo(tr.mapX(tr.xMax), py);
    }
    ctx.stroke();
    ctx.restore();
  }

  function drawPolyline(ctx, tr, points, options = {}) {
    if (!points.length) {
      return;
    }
    const {
      stroke = "#1d4ed8",
      lineWidth = 2,
      fill = null,
      close = false,
      dashed = [],
    } = options;
    ctx.save();
    ctx.setLineDash(dashed);
    ctx.lineWidth = lineWidth;
    ctx.strokeStyle = stroke;
    ctx.beginPath();
    ctx.moveTo(tr.mapX(points[0][0]), tr.mapY(points[0][1]));
    for (let i = 1; i < points.length; i += 1) {
      ctx.lineTo(tr.mapX(points[i][0]), tr.mapY(points[i][1]));
    }
    if (close) {
      ctx.closePath();
    }
    if (fill) {
      ctx.fillStyle = fill;
      ctx.fill();
    }
    ctx.stroke();
    ctx.restore();
  }

  function drawArrow(ctx, tr, x1, y1, x2, y2, options = {}) {
    const { stroke = "#1d4ed8", lineWidth = 2.2, headSize = 8, dashed = [] } = options;
    const px1 = tr.mapX(x1);
    const py1 = tr.mapY(y1);
    const px2 = tr.mapX(x2);
    const py2 = tr.mapY(y2);
    const angle = Math.atan2(py2 - py1, px2 - px1);

    ctx.save();
    ctx.setLineDash(dashed);
    ctx.strokeStyle = stroke;
    ctx.fillStyle = stroke;
    ctx.lineWidth = lineWidth;
    ctx.beginPath();
    ctx.moveTo(px1, py1);
    ctx.lineTo(px2, py2);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(px2, py2);
    ctx.lineTo(px2 - headSize * Math.cos(angle - Math.PI / 6), py2 - headSize * Math.sin(angle - Math.PI / 6));
    ctx.lineTo(px2 - headSize * Math.cos(angle + Math.PI / 6), py2 - headSize * Math.sin(angle + Math.PI / 6));
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  function drawPoint(ctx, tr, x, y, options = {}) {
    const { radius = 4, fill = "#0f172a", stroke = "#ffffff" } = options;
    ctx.save();
    ctx.fillStyle = fill;
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(tr.mapX(x), tr.mapY(y), radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }

  function matrixVector(a, b, c, d, x, y) {
    return [a * x + b * y, c * x + d * y];
  }

  function normalize(vx, vy) {
    const length = Math.hypot(vx, vy) || 1;
    return [vx / length, vy / length];
  }

  function vectorNorm(vx, vy, p) {
    if (p === "inf") {
      return Math.max(Math.abs(vx), Math.abs(vy));
    }
    const power = Number(p);
    return Math.pow(Math.pow(Math.abs(vx), power) + Math.pow(Math.abs(vy), power), 1 / power);
  }

  function pBallPoints(p, count = 260) {
    const thetas = linspace(0, Math.PI * 2, count);
    return thetas.map((theta) => {
      const c = Math.cos(theta);
      const s = Math.sin(theta);
      let radius;
      if (p === "inf") {
        radius = 1 / Math.max(Math.abs(c), Math.abs(s));
      } else {
        const power = Number(p);
        radius = Math.pow(Math.pow(Math.abs(c), power) + Math.pow(Math.abs(s), power), -1 / power);
      }
      return [radius * c, radius * s];
    });
  }

  function legendreValue(n, x) {
    if (n === 0) {
      return 1;
    }
    if (n === 1) {
      return x;
    }
    let p0 = 1;
    let p1 = x;
    for (let k = 1; k < n; k += 1) {
      const next = ((2 * k + 1) * x * p1 - k * p0) / (k + 1);
      p0 = p1;
      p1 = next;
    }
    return p1;
  }

  function hermiteValue(n, x) {
    if (n === 0) {
      return 1;
    }
    if (n === 1) {
      return 2 * x;
    }
    let h0 = 1;
    let h1 = 2 * x;
    for (let k = 1; k < n; k += 1) {
      const next = 2 * x * h1 - 2 * k * h0;
      h0 = h1;
      h1 = next;
    }
    return h1;
  }

  function initRealAnalysisDemo() {
    if (!byId("real-analysis-plot")) {
      return;
    }
    bindRange("real-freq", (v) => fmt(v, 1));
    bindRange("real-shift", (v) => fmt(v, 1));
    bindRange("real-level", (v) => fmt(v, 2));
    const note = byId("real-analysis-note");

    const render = () => {
      const freq = num(byId("real-freq").value);
      const shift = num(byId("real-shift").value);
      const level = num(byId("real-level").value);
      const xs = linspace(0, 6, 420);
      const ys = xs.map((x) => 0.85 * Math.sin(freq * x) + 0.12 * (x - 3) * (x - 1) - 0.3 + shift);

      let minIndex = 0;
      let maxIndex = 0;
      ys.forEach((value, index) => {
        if (value < ys[minIndex]) {
          minIndex = index;
        }
        if (value > ys[maxIndex]) {
          maxIndex = index;
        }
      });

      const intersections = computeIntersections(xs, ys, level);
      plotIfPresent(
        "real-analysis-plot",
        [
          {
            x: xs,
            y: ys,
            type: "scatter",
            mode: "lines",
            name: t("đồ thị f", "curve"),
            line: { color: "#1d4ed8", width: 3 },
          },
          {
            x: [0, 6],
            y: [level, level],
            type: "scatter",
            mode: "lines",
            name: t("mức c", "level c"),
            line: { color: "#be123c", dash: "dash", width: 2 },
          },
          {
            x: [xs[minIndex], xs[maxIndex]],
            y: [ys[minIndex], ys[maxIndex]],
            type: "scatter",
            mode: "markers",
            name: t("cực trị", "extrema"),
            marker: { color: "#0f766e", size: 10 },
          },
          {
            x: intersections,
            y: intersections.map(() => level),
            type: "scatter",
            mode: "markers",
            name: t("giao điểm", "intersections"),
            marker: { color: "#be123c", size: 9, symbol: "diamond" },
          },
        ],
        baseLayout({
          xaxis: { title: "x", range: [0, 6] },
          yaxis: { title: t("f(x)", "f(x)") },
        })
      );

      if (note) {
        note.textContent = t(
          `Trên đoạn đóng [0, 6], hàm liên tục này đạt min = ${fmt(ys[minIndex])} và max = ${fmt(ys[maxIndex])}. Đường y = ${fmt(level)} cắt đồ thị ${intersections.length} lần, nên người học nhìn thấy đồng thời định lý cực trị và ý tưởng giá trị trung gian.`,
          `On the closed interval [0, 6], this continuous curve attains min = ${fmt(ys[minIndex])} and max = ${fmt(ys[maxIndex])}. The line y = ${fmt(level)} meets the graph ${intersections.length} time(s), so the picture reinforces both extrema on compact sets and the intermediate-value idea.`
        );
      }
    };

    attachRender(["real-freq", "real-shift", "real-level"], render);
  }

  function initUniformContinuityDemo() {
    if (!byId("uniform-plot")) {
      return;
    }
    bindRange("uniform-L", (v) => fmt(v, 1));
    bindRange("uniform-delta", (v) => fmt(v, 2));
    bindRange("uniform-epsilon", (v) => fmt(v, 2));
    const note = byId("uniform-note");
    const functions = {
      square: {
        label: "x^2",
        fn: (x) => x * x,
      },
      sine: {
        label: "sin x",
        fn: (x) => Math.sin(x),
      },
      arctan: {
        label: "arctan x",
        fn: (x) => Math.atan(x),
      },
    };

    const render = () => {
      const key = byId("uniform-function").value;
      const config = functions[key];
      const L = num(byId("uniform-L").value);
      const delta = num(byId("uniform-delta").value);
      const epsilon = num(byId("uniform-epsilon").value);
      const f = config.fn;
      const xs = linspace(-L, L, 420);
      const ys = xs.map(f);
      const xA = 0;
      const xB = L - delta;
      const yA1 = f(xA);
      const yA2 = f(xA + delta);
      const yB1 = f(xB);
      const yB2 = f(xB + delta);
      const diffA = Math.abs(yA2 - yA1);
      const diffB = Math.abs(yB2 - yB1);

      plotIfPresent(
        "uniform-plot",
        [
          {
            x: xs,
            y: ys,
            type: "scatter",
            mode: "lines",
            name: config.label,
            line: { color: "#1d4ed8", width: 3 },
          },
          {
            x: [xA, xA + delta],
            y: [yA1, yA2],
            type: "scatter",
            mode: "markers+lines",
            name: t("cặp gần gốc", "central pair"),
            line: { color: "#0f766e", width: 2 },
            marker: { size: 9, color: "#0f766e" },
          },
          {
            x: [xB, xB + delta],
            y: [yB1, yB2],
            type: "scatter",
            mode: "markers+lines",
            name: t("cặp gần biên", "edge pair"),
            line: { color: "#be123c", width: 2 },
            marker: { size: 9, color: "#be123c" },
          },
        ],
        baseLayout({
          xaxis: { title: "x", range: [-L, L] },
          yaxis: { title: t("f(x)", "f(x)") },
        })
      );

      if (note) {
        const success = diffA < epsilon && diffB < epsilon;
        note.textContent = t(
          `Với cùng một delta = ${fmt(delta)}, ta có |Δf| gần gốc ≈ ${fmt(diffA)} và gần biên ≈ ${fmt(diffB)}. So với epsilon = ${fmt(epsilon)}, kết luận hiện tại là ${success ? "đạt" : "không đạt"} một kiểm soát đồng đều trên cửa sổ đang xem.`,
          `Using the same delta = ${fmt(delta)}, we get |Δf| near the center ≈ ${fmt(diffA)} and near the edge ≈ ${fmt(diffB)}. Compared against epsilon = ${fmt(epsilon)}, the current window ${success ? "does" : "does not"} support a uniform estimate.`
        );
      }
    };

    attachRender(["uniform-function", "uniform-L", "uniform-delta", "uniform-epsilon"], render);
  }

  function initMultivariableDemo() {
    if (!byId("multivariable-plot")) {
      return;
    }
    bindRange("multi-a", (v) => fmt(v, 1));
    bindRange("multi-b", (v) => fmt(v, 1));
    bindRange("multi-c", (v) => fmt(v, 1));
    bindRange("multi-x", (v) => fmt(v, 1));
    bindRange("multi-y", (v) => fmt(v, 1));
    const note = byId("multivariable-note");

    const render = () => {
      const a = num(byId("multi-a").value);
      const b = num(byId("multi-b").value);
      const c = num(byId("multi-c").value);
      const x0 = num(byId("multi-x").value);
      const y0 = num(byId("multi-y").value);
      const xs = linspace(-2.5, 2.5, 45);
      const ys = linspace(-2.5, 2.5, 45);
      const surface = ys.map((y) => xs.map((x) => a * x * x + b * y * y + c * x * y));
      const gx = 2 * a * x0 + c * y0;
      const gy = 2 * b * y0 + c * x0;
      const gradNorm = Math.hypot(gx, gy);
      const scale = gradNorm > 1e-8 ? 0.65 / gradNorm : 0;
      const dx = gx * scale;
      const dy = gy * scale;

      plotIfPresent(
        "multivariable-plot",
        [
          {
            x: xs,
            y: ys,
            z: surface,
            type: "contour",
            colorscale: [
              [0, "#eff6ff"],
              [0.45, "#93c5fd"],
              [1, "#1d4ed8"],
            ],
            line: { width: 0.6, color: "#cbd5e1" },
            contours: { coloring: "heatmap" },
            showscale: false,
            name: t("mức", "levels"),
          },
          {
            x: [x0],
            y: [y0],
            type: "scatter",
            mode: "markers",
            name: t("điểm đang xét", "selected point"),
            marker: { size: 11, color: "#be123c" },
          },
        ],
        baseLayout({
          xaxis: { title: "x", range: [-2.5, 2.5] },
          yaxis: { title: "y", range: [-2.5, 2.5], scaleanchor: "x", scaleratio: 1 },
          annotations: gradNorm > 1e-8
            ? [
                {
                  x: x0 + dx,
                  y: y0 + dy,
                  ax: x0,
                  ay: y0,
                  axref: "x",
                  ayref: "y",
                  text: t("gradient", "gradient"),
                  showarrow: true,
                  arrowhead: 3,
                  arrowsize: 1,
                  arrowwidth: 2,
                  arrowcolor: "#be123c",
                  font: { size: 11, color: "#be123c" },
                },
              ]
            : [],
        })
      );

      if (note) {
        note.textContent = t(
          `Tại điểm (${fmt(x0, 1)}, ${fmt(y0, 1)}), gradient là (${fmt(gx)}, ${fmt(gy)}) với độ lớn ${fmt(gradNorm)}. Vector này chỉ hướng tăng nhanh nhất của hàm và là bản đồ trực giác cho Jacobian hoặc tuyến tính hóa cục bộ trong nhiều biến.`,
          `At (${fmt(x0, 1)}, ${fmt(y0, 1)}), the gradient is (${fmt(gx)}, ${fmt(gy)}) with magnitude ${fmt(gradNorm)}. That vector points in the direction of steepest increase and gives a clean visual entry point to Jacobians and local linearization.`
        );
      }
    };

    attachRender(["multi-a", "multi-b", "multi-c", "multi-x", "multi-y"], render);
  }

  function initLinearAlgebraDemo() {
    const canvas = byId("linear-canvas");
    if (!canvas) {
      return;
    }
    bindRange("lin-a", (v) => fmt(v, 1));
    bindRange("lin-b", (v) => fmt(v, 1));
    bindRange("lin-c", (v) => fmt(v, 1));
    bindRange("lin-d", (v) => fmt(v, 1));
    const note = byId("linear-note");

    function eigenvectorFor(lambda, a, b, c, d) {
      if (Math.abs(b) > 1e-8) {
        return normalize(lambda - d, b);
      }
      if (Math.abs(c) > 1e-8) {
        return normalize(c, lambda - a);
      }
      if (Math.abs(lambda - a) < Math.abs(lambda - d)) {
        return [1, 0];
      }
      return [0, 1];
    }

    const render = () => {
      const a = num(byId("lin-a").value);
      const b = num(byId("lin-b").value);
      const c = num(byId("lin-c").value);
      const d = num(byId("lin-d").value);
      const ctx = clearCanvas(canvas);
      const tr = makeTransform({ canvas, xMin: -4, xMax: 4, yMin: -4, yMax: 4, padding: 34 });
      drawGrid(ctx, tr, 1, 1);
      drawAxes(ctx, tr);

      const circle = linspace(0, Math.PI * 2, 220).map((theta) => [Math.cos(theta), Math.sin(theta)]);
      drawPolyline(ctx, tr, circle, { stroke: "#cbd5e1", lineWidth: 1.5, close: true });

      const ellipse = circle.map(([x, y]) => matrixVector(a, b, c, d, x, y));
      drawPolyline(ctx, tr, ellipse, {
        stroke: "#1d4ed8",
        lineWidth: 2.4,
        fill: "rgba(29, 78, 216, 0.08)",
        close: true,
      });

      drawPolyline(ctx, tr, [[0, 0], [1, 0], [1, 1], [0, 1]], {
        stroke: "#94a3b8",
        lineWidth: 1.5,
        dashed: [5, 4],
        close: true,
      });
      const transformedSquare = [[0, 0], matrixVector(a, b, c, d, 1, 0), matrixVector(a, b, c, d, 1, 1), matrixVector(a, b, c, d, 0, 1)];
      drawPolyline(ctx, tr, transformedSquare, {
        stroke: "#0f766e",
        lineWidth: 2.2,
        fill: "rgba(15, 118, 110, 0.10)",
        close: true,
      });

      drawArrow(ctx, tr, 0, 0, a, c, { stroke: "#1d4ed8" });
      drawArrow(ctx, tr, 0, 0, b, d, { stroke: "#0f766e" });
      drawPoint(ctx, tr, 0, 0, { fill: "#0f172a" });

      const trace = a + d;
      const det = a * d - b * c;
      const disc = trace * trace - 4 * det;
      if (disc >= 0) {
        const root = Math.sqrt(disc);
        const lambda1 = 0.5 * (trace + root);
        const lambda2 = 0.5 * (trace - root);
        const v1 = eigenvectorFor(lambda1, a, b, c, d);
        const v2 = eigenvectorFor(lambda2, a, b, c, d);
        drawPolyline(ctx, tr, [[-3.6 * v1[0], -3.6 * v1[1]], [3.6 * v1[0], 3.6 * v1[1]]], {
          stroke: "#b45309",
          lineWidth: 1.8,
          dashed: [8, 5],
        });
        drawPolyline(ctx, tr, [[-3.6 * v2[0], -3.6 * v2[1]], [3.6 * v2[0], 3.6 * v2[1]]], {
          stroke: "#be123c",
          lineWidth: 1.8,
          dashed: [8, 5],
        });
        if (note) {
          note.textContent = t(
            `trace = ${fmt(trace)}, det = ${fmt(det)}, trị riêng ≈ ${fmt(lambda1)} và ${fmt(lambda2)}. Các đường đứt là hướng riêng thực, nên người học thấy ngay khi nào ma trận kéo giãn dọc theo các phương bất biến.`,
            `trace = ${fmt(trace)}, det = ${fmt(det)}, eigenvalues ≈ ${fmt(lambda1)} and ${fmt(lambda2)}. The dashed lines mark real eigendirections, so the picture shows when a matrix stretches space along invariant directions.`
          );
        }
      } else if (note) {
        note.textContent = t(
          `trace = ${fmt(trace)}, det = ${fmt(det)} và biệt thức < 0, nên hiện tại không có hướng riêng thực. Khi đó phép biến đổi thiên về quay-kéo thay vì tách rõ theo các trục bất biến thực.`,
          `trace = ${fmt(trace)}, det = ${fmt(det)}, and the discriminant is negative, so there are no real eigendirections here. The map behaves more like a coupled rotate-and-stretch transformation than a clean split along real invariant lines.`
        );
      }
    };

    attachRender(["lin-a", "lin-b", "lin-c", "lin-d"], render);
  }

  function initComplexDemo() {
    if (!byId("complex-plot")) {
      return;
    }
    bindRange("complex-alpha", (v) => fmt(v, 2));
    bindRange("complex-beta", (v) => fmt(v, 1));
    bindRange("complex-time", (v) => fmt(v, 1));
    const note = byId("complex-note");

    const render = () => {
      const alpha = num(byId("complex-alpha").value);
      const beta = num(byId("complex-beta").value);
      const time = num(byId("complex-time").value);
      const ts = linspace(0, 8, 360);
      const re = ts.map((s) => Math.exp(alpha * s) * Math.cos(beta * s));
      const im = ts.map((s) => Math.exp(alpha * s) * Math.sin(beta * s));
      const currentRadius = Math.exp(alpha * time);
      const currentRe = currentRadius * Math.cos(beta * time);
      const currentIm = currentRadius * Math.sin(beta * time);
      const limit = Math.max(1.2, ...re.map(Math.abs), ...im.map(Math.abs)) * 1.12;

      plotIfPresent(
        "complex-plot",
        [
          {
            x: re,
            y: im,
            type: "scatter",
            mode: "lines",
            name: t("quỹ đạo", "trajectory"),
            line: { color: "#1d4ed8", width: 3 },
          },
          {
            x: [currentRe],
            y: [currentIm],
            type: "scatter",
            mode: "markers",
            name: t("điểm tại thời gian t", "point at time t"),
            marker: { color: "#be123c", size: 12 },
          },
        ],
        baseLayout({
          xaxis: { title: t("phần thực", "real part"), range: [-limit, limit] },
          yaxis: {
            title: t("phần ảo", "imaginary part"),
            range: [-limit, limit],
            scaleanchor: "x",
            scaleratio: 1,
          },
          shapes: [
            {
              type: "circle",
              xref: "x",
              yref: "y",
              x0: -currentRadius,
              x1: currentRadius,
              y0: -currentRadius,
              y1: currentRadius,
              line: { color: "rgba(15, 118, 110, 0.45)", dash: "dot" },
            },
          ],
        })
      );

      if (note) {
        note.textContent = t(
          `Tại t = ${fmt(time, 1)}, ta có z(t) ≈ ${fmt(currentRe)} + ${fmt(currentIm)}i và |z(t)| = e^(alpha t) ≈ ${fmt(currentRadius)}. Beta điều khiển tốc độ quay, còn alpha điều khiển việc spiral co vào hay bung ra.`,
          `At t = ${fmt(time, 1)}, z(t) ≈ ${fmt(currentRe)} + ${fmt(currentIm)}i and |z(t)| = e^(alpha t) ≈ ${fmt(currentRadius)}. Beta controls the rotation rate, while alpha determines whether the spiral decays inward or grows outward.`
        );
      }
    };

    attachRender(["complex-alpha", "complex-beta", "complex-time"], render);
  }

  function initMetricDemo() {
    const canvas = byId("metric-canvas");
    if (!canvas) {
      return;
    }
    bindRange("metric-cx", (v) => fmt(v, 1));
    bindRange("metric-cy", (v) => fmt(v, 1));
    bindRange("metric-r", (v) => fmt(v, 2));
    const note = byId("metric-note");

    const render = () => {
      const cx = num(byId("metric-cx").value);
      const cy = num(byId("metric-cy").value);
      const r = num(byId("metric-r").value);
      const ctx = clearCanvas(canvas);

      const gap = 16;
      const panelWidth = (canvas.width - gap * 4) / 3;
      const panelHeight = canvas.height - 34;
      const metrics = [
        {
          title: t("Euclid d2", "Euclidean d2"),
          points: linspace(0, Math.PI * 2, 200).map((theta) => [cx + r * Math.cos(theta), cy + r * Math.sin(theta)]),
          fill: "rgba(29, 78, 216, 0.10)",
          stroke: "#1d4ed8",
        },
        {
          title: t("Taxi d1", "Taxicab d1"),
          points: [[cx, cy + r], [cx + r, cy], [cx, cy - r], [cx - r, cy]],
          fill: "rgba(15, 118, 110, 0.10)",
          stroke: "#0f766e",
        },
        {
          title: t("Chebyshev dinf", "Chebyshev dinf"),
          points: [[cx - r, cy - r], [cx + r, cy - r], [cx + r, cy + r], [cx - r, cy + r]],
          fill: "rgba(190, 18, 60, 0.10)",
          stroke: "#be123c",
        },
      ];

      metrics.forEach((metric, index) => {
        const tr = makeTransform({
          canvas,
          left: gap + index * (panelWidth + gap),
          top: 14,
          width: panelWidth,
          height: panelHeight,
          xMin: -3,
          xMax: 3,
          yMin: -3,
          yMax: 3,
          padding: 28,
        });
        drawPanelFrame(ctx, tr, metric.title);
        drawGrid(ctx, tr, 1, 1);
        drawAxes(ctx, tr);
        drawPolyline(ctx, tr, metric.points, {
          stroke: metric.stroke,
          lineWidth: 2.1,
          fill: metric.fill,
          close: true,
        });
        drawPoint(ctx, tr, cx, cy, { fill: metric.stroke });
      });

      if (note) {
        note.textContent = t(
          `Cùng tâm (${fmt(cx, 1)}, ${fmt(cy, 1)}) và cùng bán kính ${fmt(r)}, ba "quả cầu mở" nhìn rất khác nhau vì metric thay đổi chính định nghĩa khoảng cách. Đây là bước chuyển từ trực giác Euclid sang không gian metric trừu tượng.`,
          `With the same center (${fmt(cx, 1)}, ${fmt(cy, 1)}) and radius ${fmt(r)}, the three balls look different because the metric changes the very definition of distance. That is the conceptual jump from Euclidean pictures to abstract metric spaces.`
        );
      }
    };

    attachRender(["metric-cx", "metric-cy", "metric-r"], render);
  }

  function initNormDemo() {
    const canvas = byId("norm-canvas");
    if (!canvas) {
      return;
    }
    bindRange("norm-x", (v) => fmt(v, 1));
    bindRange("norm-y", (v) => fmt(v, 1));
    const note = byId("norm-note");

    const render = () => {
      const p = byId("norm-p").value;
      const vx = num(byId("norm-x").value);
      const vy = num(byId("norm-y").value);
      const ctx = clearCanvas(canvas);
      const tr = makeTransform({ canvas, xMin: -2.2, xMax: 2.2, yMin: -2.2, yMax: 2.2, padding: 34 });
      drawGrid(ctx, tr, 0.5, 0.5);
      drawAxes(ctx, tr);

      const ball = pBallPoints(p);
      drawPolyline(ctx, tr, ball, {
        stroke: "#1d4ed8",
        lineWidth: 2.4,
        fill: "rgba(29, 78, 216, 0.08)",
        close: true,
      });

      const norm = vectorNorm(vx, vy, p);
      const boundary = norm > 1e-8 ? [vx / norm, vy / norm] : [0, 0];
      drawArrow(ctx, tr, 0, 0, vx, vy, { stroke: "#0f766e" });
      drawArrow(ctx, tr, 0, 0, boundary[0], boundary[1], { stroke: "#be123c", dashed: [6, 4] });
      drawPoint(ctx, tr, boundary[0], boundary[1], { fill: "#be123c" });

      if (note) {
        const label = p === "inf" ? "L∞" : `L${p}`;
        note.textContent = t(
          `Trong chuẩn ${label}, vector v = (${fmt(vx, 1)}, ${fmt(vy, 1)}) có độ lớn ||v|| ≈ ${fmt(norm)}. Mũi tên đứt đưa v về biên của quả cầu đơn vị, nên sinh viên thấy ngay "độ lớn" phụ thuộc vào chuẩn chứ không chỉ vào tọa độ.`,
          `In the ${label} norm, v = (${fmt(vx, 1)}, ${fmt(vy, 1)}) has size ||v|| ≈ ${fmt(norm)}. The dashed arrow rescales v back to the unit-ball boundary, making it visually clear that magnitude depends on the chosen norm, not only on coordinates.`
        );
      }
    };

    attachRender(["norm-p", "norm-x", "norm-y"], render);
  }

  function initProjectionDemo() {
    const canvas = byId("projection-canvas");
    if (!canvas) {
      return;
    }
    bindRange("proj-angle", (v) => `${fmt(v, 0)}°`);
    bindRange("proj-x", (v) => fmt(v, 1));
    bindRange("proj-y", (v) => fmt(v, 1));
    const note = byId("projection-note");

    const render = () => {
      const angle = (num(byId("proj-angle").value) * Math.PI) / 180;
      const vx = num(byId("proj-x").value);
      const vy = num(byId("proj-y").value);
      const ux = Math.cos(angle);
      const uy = Math.sin(angle);
      const scalar = vx * ux + vy * uy;
      const px = scalar * ux;
      const py = scalar * uy;
      const rx = vx - px;
      const ry = vy - py;

      const ctx = clearCanvas(canvas);
      const tr = makeTransform({ canvas, xMin: -3, xMax: 3, yMin: -3, yMax: 3, padding: 34 });
      drawGrid(ctx, tr, 1, 1);
      drawAxes(ctx, tr);
      drawPolyline(ctx, tr, [[-3 * ux, -3 * uy], [3 * ux, 3 * uy]], {
        stroke: "#94a3b8",
        lineWidth: 2,
      });
      drawArrow(ctx, tr, 0, 0, vx, vy, { stroke: "#1d4ed8" });
      drawArrow(ctx, tr, 0, 0, px, py, { stroke: "#0f766e" });
      drawArrow(ctx, tr, px, py, vx, vy, { stroke: "#b45309", dashed: [6, 4] });
      drawPoint(ctx, tr, px, py, { fill: "#0f766e" });

      if (note) {
        note.textContent = t(
          `Hình chiếu của v lên đường sinh bởi u có độ dài vô hướng ≈ ${fmt(scalar)}; phần dư có chuẩn ≈ ${fmt(Math.hypot(rx, ry))}. Đây chính là trực giác của trực giao, bình phương tối thiểu và không gian Hilbert.`,
          `The scalar projection of v onto the line spanned by u is ≈ ${fmt(scalar)}, and the residual has norm ≈ ${fmt(Math.hypot(rx, ry))}. This is the geometric core of orthogonality, least squares, and Hilbert-space thinking.`
        );
      }
    };

    attachRender(["proj-angle", "proj-x", "proj-y"], render);
  }

  function initIntegrationDemo() {
    const canvas = byId("integration-canvas");
    if (!canvas) {
      return;
    }
    bindRange("int-n", (v) => fmt(v, 0));
    const note = byId("integration-note");
    const functions = {
      sine: {
        label: t("1 + 0.8 sin(1.4x)", "1 + 0.8 sin(1.4x)"),
        fn: (x) => 1 + 0.8 * Math.sin(1.4 * x),
      },
      gaussian: {
        label: t("0.4 + exp(-0.8(x-1.2)^2)", "0.4 + exp(-0.8(x-1.2)^2)"),
        fn: (x) => 0.4 + Math.exp(-0.8 * (x - 1.2) * (x - 1.2)),
      },
      quadratic: {
        label: t("0.3 + 0.25x + 0.12x^2", "0.3 + 0.25x + 0.12x^2"),
        fn: (x) => 0.3 + 0.25 * x + 0.12 * x * x,
      },
    };

    const render = () => {
      const key = byId("int-function").value;
      const rule = byId("int-rule").value;
      const n = Math.max(2, Math.round(num(byId("int-n").value)));
      const { fn, label } = functions[key];
      const a = 0;
      const b = 3;
      const h = (b - a) / n;
      const fineXs = linspace(a, b, 360);
      const fineYs = fineXs.map(fn);
      const yMax = Math.max(...fineYs) * 1.18;
      const ctx = clearCanvas(canvas);
      const tr = makeTransform({ canvas, xMin: a, xMax: b, yMin: 0, yMax, padding: 34 });
      drawGrid(ctx, tr, 0.5, 0.5);
      drawAxes(ctx, tr);

      let approx = 0;
      for (let i = 0; i < n; i += 1) {
        const xL = a + i * h;
        const xR = xL + h;
        if (rule === "trap") {
          const yL = fn(xL);
          const yR = fn(xR);
          approx += 0.5 * h * (yL + yR);
          drawPolyline(ctx, tr, [[xL, 0], [xL, yL], [xR, yR], [xR, 0]], {
            stroke: "#c084fc",
            lineWidth: 1.2,
            fill: "rgba(192, 132, 252, 0.14)",
            close: true,
          });
        } else {
          const sample = rule === "left" ? xL : xL + 0.5 * h;
          const y = fn(sample);
          approx += h * y;
          drawPolyline(ctx, tr, [[xL, 0], [xL, y], [xR, y], [xR, 0]], {
            stroke: "#93c5fd",
            lineWidth: 1.2,
            fill: "rgba(59, 130, 246, 0.14)",
            close: true,
          });
        }
      }

      drawPolyline(
        ctx,
        tr,
        fineXs.map((x) => [x, fn(x)]),
        { stroke: "#1d4ed8", lineWidth: 2.6 }
      );

      const exact = approxIntegral(fn, a, b, 3000);
      if (note) {
        note.textContent = t(
          `Hàm đang xét là ${label}. Với n = ${n} phần và quy tắc ${rule === "left" ? "trái" : rule === "mid" ? "trung điểm" : "hình thang"}, giá trị gần đúng ≈ ${fmt(approx)}; tham chiếu mịn ≈ ${fmt(exact)}; sai số ≈ ${fmt(Math.abs(approx - exact))}.`,
          `For ${label} with n = ${n} subintervals and the ${rule === "left" ? "left-endpoint" : rule === "mid" ? "midpoint" : "trapezoidal"} rule, the approximation is ≈ ${fmt(approx)}; a fine-grid reference gives ≈ ${fmt(exact)}; the current error is ≈ ${fmt(Math.abs(approx - exact))}.`
        );
      }
    };

    attachRender(["int-function", "int-rule", "int-n"], render);
  }

  function initVectorFieldDemo() {
    const canvas = byId("vector-canvas");
    if (!canvas) {
      return;
    }
    bindRange("vf-sx", (v) => fmt(v, 1));
    bindRange("vf-sy", (v) => fmt(v, 1));
    bindRange("vf-rot", (v) => fmt(v, 1));
    const note = byId("vector-note");

    const render = () => {
      const sx = num(byId("vf-sx").value);
      const sy = num(byId("vf-sy").value);
      const rot = num(byId("vf-rot").value);
      const ctx = clearCanvas(canvas);
      const tr = makeTransform({ canvas, xMin: -2.4, xMax: 2.4, yMin: -2.4, yMax: 2.4, padding: 34 });
      drawGrid(ctx, tr, 0.6, 0.6);
      drawAxes(ctx, tr);

      for (let x = -1.8; x <= 1.8 + 1e-8; x += 0.6) {
        for (let y = -1.8; y <= 1.8 + 1e-8; y += 0.6) {
          const fx = sx * x - rot * y;
          const fy = rot * x + sy * y;
          const magnitude = Math.hypot(fx, fy);
          if (magnitude < 1e-8) {
            drawPoint(ctx, tr, x, y, { radius: 2.5, fill: "#64748b" });
            continue;
          }
          const scale = 0.26 / (1 + 0.25 * magnitude);
          drawArrow(ctx, tr, x, y, x + scale * fx, y + scale * fy, {
            stroke: "#1d4ed8",
            lineWidth: 1.8,
            headSize: 6,
          });
        }
      }

      const divergence = sx + sy;
      const curl = 2 * rot;
      const radialText =
        divergence > 0.15 ? t("nguồn lan ra", "source-like spreading") :
        divergence < -0.15 ? t("hút vào kiểu sink", "sink-like contraction") :
        t("gần như không nén/giãn", "almost area-balanced");
      const swirlText =
        Math.abs(curl) > 0.2 ? t("có xoáy rõ", "clear rotational tendency") : t("xoáy yếu", "little rotation");

      if (note) {
        note.textContent = t(
          `div F = ${fmt(divergence)} và curl F = ${fmt(curl)}. Trường hiện tại biểu hiện ${radialText}, đồng thời ${swirlText}. Đây là cách trực quan nhất để tách hai hiệu ứng "phình/co" và "quay" trong giải tích vector.`,
          `div F = ${fmt(divergence)} and curl F = ${fmt(curl)}. The current field is ${radialText} with ${swirlText}. This is the cleanest picture for separating expansion/contraction from rotation in vector calculus.`
        );
      }
    };

    attachRender(["vf-sx", "vf-sy", "vf-rot"], render);
  }

  function initSpecialFunctionsDemo() {
    if (!byId("special-plot")) {
      return;
    }
    bindRange("spec-n", (v) => fmt(v, 0));
    bindRange("spec-m", (v) => fmt(v, 0));
    const note = byId("special-note");

    const render = () => {
      const family = byId("spec-family").value;
      const n = Math.round(num(byId("spec-n").value));
      const m = Math.round(num(byId("spec-m").value));
      const isLegendre = family === "legendre";
      const fn = isLegendre ? legendreValue : hermiteValue;
      const a = isLegendre ? -1 : -3;
      const b = isLegendre ? 1 : 3;
      const weight = isLegendre ? () => 1 : (x) => Math.exp(-x * x);
      const xs = linspace(a, b, 420);
      const yn = xs.map((x) => fn(n, x));
      const ym = xs.map((x) => fn(m, x));
      const innerProduct = approxIntegral((x) => fn(n, x) * fn(m, x), a, b, 2600, weight);
      const labelN = isLegendre ? `P_${n}` : `H_${n}`;
      const labelM = isLegendre ? `P_${m}` : `H_${m}`;

      plotIfPresent(
        "special-plot",
        [
          {
            x: xs,
            y: yn,
            type: "scatter",
            mode: "lines",
            name: labelN,
            line: { color: "#1d4ed8", width: 3 },
          },
          {
            x: xs,
            y: ym,
            type: "scatter",
            mode: "lines",
            name: labelM,
            line: { color: "#be123c", width: 2.4, dash: "dash" },
          },
        ],
        baseLayout({
          xaxis: { title: "x", range: [a, b] },
          yaxis: { title: t("giá trị", "value") },
        })
      );

      if (note) {
        note.textContent = t(
          `${isLegendre ? "Họ Legendre" : "Họ Hermite"} cho thấy special functions không phải các công thức lẻ tẻ mà là những gia đình có cấu trúc. Tích vô hướng có trọng số giữa ${labelN} và ${labelM} hiện xấp xỉ ${fmt(innerProduct)}, nên ta thấy trực tiếp hiện tượng trực giao theo bậc.`,
          `The ${isLegendre ? "Legendre" : "Hermite"} family shows that special functions are not isolated formulas but structured sequences. The weighted inner product between ${labelN} and ${labelM} is currently about ${fmt(innerProduct)}, so the plot makes orthogonality by order visible.`
        );
      }
    };

    attachRender(["spec-family", "spec-n", "spec-m"], render);
  }

  window.addEventListener("load", () => {
    initRealAnalysisDemo();
    initUniformContinuityDemo();
    initMultivariableDemo();
    initLinearAlgebraDemo();
    initComplexDemo();
    initMetricDemo();
    initNormDemo();
    initProjectionDemo();
    initIntegrationDemo();
    initVectorFieldDemo();
    initSpecialFunctionsDemo();
  });
})();
