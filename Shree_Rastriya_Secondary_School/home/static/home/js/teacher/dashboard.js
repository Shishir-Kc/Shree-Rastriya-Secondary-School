document.addEventListener("DOMContentLoaded", () => {
    // Sidebar Toggle
    const sidebarToggle = document.getElementById("sidebar-toggle")
    const sidebar = document.querySelector(".sidebar")
  
    sidebarToggle.addEventListener("click", (e) => {
      e.stopPropagation()
      sidebar.classList.toggle("active")
      sidebarToggle.classList.toggle("is-active")
    })
  
    function closeSidebar() {
      if (window.innerWidth <= 768 && sidebar.classList.contains("active")) {
        sidebar.classList.remove("active")
      }
    }
  
    // Add click event listener to the document
    document.addEventListener("click", (e) => {
      if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
        closeSidebar()
      }
    })
  
    // Add resize event listener to handle responsiveness
    window.addEventListener("resize", () => {
      if (window.innerWidth > 768) {
        sidebar.classList.remove("active")
      }
    })
  
    // Floating Menu Toggle with Animations
    const floatingMenu = document.querySelector(".floating-menu")
    const floatingBtn = floatingMenu.querySelector(".floating-btn")
    const floatingOptions = floatingMenu.querySelectorAll(".floating-option")
  
    function fadeInOptions() {
      floatingOptions.forEach((option, index) => {
        setTimeout(() => {
          option.style.opacity = "1"
          option.style.transform = "scale(1) translateY(0)"
        }, index * 100)
      })
    }
  
    function fadeOutOptions() {
      ;[...floatingOptions].reverse().forEach((option, index) => {
        setTimeout(() => {
          option.style.opacity = "0"
          option.style.transform = "scale(0.5) translateY(20px)"
        }, index * 100)
      })
    }
  
    function toggleMenu() {
      if (floatingMenu.classList.contains("open")) {
        fadeOutOptions()
        setTimeout(() => {
          floatingMenu.classList.remove("open")
        }, floatingOptions.length * 100)
      } else {
        floatingMenu.classList.add("open")
        fadeInOptions()
      }
    }
  
    floatingBtn.addEventListener("click", (e) => {
      e.stopPropagation()
      toggleMenu()
    })
  
    // Close floating menu when clicking outside
    document.addEventListener("click", (e) => {
      if (floatingMenu.classList.contains("open") && !floatingMenu.contains(e.target)) {
        toggleMenu()
      }
    })
  
    // Add hover effect to cards
    const cards = document.querySelectorAll(".card, .stat-card")
    cards.forEach((card) => {
      card.addEventListener("mouseover", () => {
        card.style.transform = "translateY(-5px)"
      })
  
      card.addEventListener("mouseout", () => {
        card.style.transform = "translateY(0)"
      })
    })
  
    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()
        document.querySelector(this.getAttribute("href")).scrollIntoView({
          behavior: "smooth",
        })
      })
    })
  })
  
  