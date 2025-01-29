document.addEventListener("DOMContentLoaded", () => {
    const mainContent = document.querySelector(".main-content")
    const notesContainer = document.querySelector(".notes-container")
  
    // Smooth scroll function
    function smoothScroll(target, duration) {
      const targetPosition = target.getBoundingClientRect().top
      const startPosition = mainContent.scrollTop
      const distance = targetPosition - startPosition
      let startTime = null
  
      function animation(currentTime) {
        if (startTime === null) startTime = currentTime
        const timeElapsed = currentTime - startTime
        const run = ease(timeElapsed, startPosition, distance, duration)
        mainContent.scrollTop = run
        if (timeElapsed < duration) requestAnimationFrame(animation)
      }
  
      function ease(t, b, c, d) {
        t /= d / 2
        if (t < 1) return (c / 2) * t * t + b
        t--
        return (-c / 2) * (t * (t - 2) - 1) + b
      }
  
      requestAnimationFrame(animation)
    }
  
    // Add click event listeners to note sections
    const notesSections = document.querySelectorAll(".notes-section")
    notesSections.forEach((section) => {
      section.addEventListener("click", function () {
        smoothScroll(this, 500)
      })
    })
  
    // Intersection Observer for lazy loading and animations
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible")
          } else {
            entry.target.classList.remove("visible")
          }
        })
      },
      {
        root: mainContent,
        threshold: 0.1,
      },
    )
  
    notesSections.forEach((section) => {
      observer.observe(section)
    })
  
    // Initialize Lucide icons
    // Assuming Lucide is available via a CDN or a module import.  Replace with your actual import.
    // For example, if using a CDN:
    // <script type="module" src="https://cdn.skypack.dev/@lucide/react"></script>
  
    // Or if using a module bundler like Webpack or Parcel:
    // import * as lucide from '@lucide/react'; // Or the correct import path
  
    lucide.createIcons()
  })
  
  