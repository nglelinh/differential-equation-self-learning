(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');

  if (window.innerWidth > 1480)
    checkbox.checked = true;

  document.addEventListener('click', function(e) {
    var target = e.target;

    if(!checkbox.checked ||
       sidebar.contains(target) ||
       (target === checkbox || target === toggle)) return;

    checkbox.checked = false;
  }, false);

  // Chapter submenu toggle functionality
  document.addEventListener('DOMContentLoaded', function() {
    var chapterToggles = document.querySelectorAll('.sidebar-chapter-toggle');
    
    chapterToggles.forEach(function(toggleBtn) {
      toggleBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        
        var chapter = this.closest('.sidebar-chapter');
        var submenu = chapter.querySelector('.sidebar-submenu');
        
        // Toggle the expanded state
        chapter.classList.toggle('expanded');
        
        // Toggle the submenu open state
        if (submenu) {
          submenu.classList.toggle('open');
        }
      });
    });
    
    // Also allow clicking the chapter header (but not the link) to toggle
    var chapterHeaders = document.querySelectorAll('.sidebar-chapter-header');
    
    chapterHeaders.forEach(function(header) {
      header.addEventListener('click', function(e) {
        // Only toggle if clicking outside the link
        if (!e.target.closest('.sidebar-chapter-link')) {
          e.preventDefault();
          
          var chapter = this.closest('.sidebar-chapter');
          var submenu = chapter.querySelector('.sidebar-submenu');
          
          chapter.classList.toggle('expanded');
          
          if (submenu) {
            submenu.classList.toggle('open');
          }
        }
      });
    });
  });
})(document);
