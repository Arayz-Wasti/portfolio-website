document.addEventListener('DOMContentLoaded', () => {
    // 1. Typing Animation
    const typedTextSpan = document.querySelector(".typed-text");
    const cursorSpan = document.querySelector(".cursor");

    const textArray = ["Backend Developer", "API Architect", "Python Specialist", "Automation Wizard"];
    const typingDelay = 100;
    const erasingDelay = 50;
    const newTextDelay = 2000;
    let textArrayIndex = 0;
    let charIndex = 0;

    function type() {
        if (charIndex < textArray[textArrayIndex].length) {
            if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
            typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
            charIndex++;
            setTimeout(type, typingDelay);
        } else {
            cursorSpan.classList.remove("typing");
            setTimeout(erase, newTextDelay);
        }
    }

    function erase() {
        if (charIndex > 0) {
            if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
            typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(erase, erasingDelay);
        } else {
            cursorSpan.classList.remove("typing");
            textArrayIndex++;
            if (textArrayIndex >= textArray.length) textArrayIndex = 0;
            setTimeout(type, typingDelay + 1100);
        }
    }

    if (textArray.length) setTimeout(type, newTextDelay + 250);

    // 2. Smooth Scrolling & Active Link
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 150) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(current)) {
                link.classList.add("active");
            }
        });
    });

    // 3. Contact Form Submission (AJAX)
    const contactForm = document.getElementById("contact-form");
    const formMessage = document.getElementById("form-message");

    if (contactForm) {
        contactForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(contactForm);

            try {
                const response = await fetch("/contact/submit/", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": formData.get("csrfmiddlewaretoken")
                    }
                });

                const data = await response.json();

                formMessage.textContent = data.message;
                formMessage.className = data.status === "success" ? "success-msg" : "error-msg";
                formMessage.classList.remove("hidden");

                if (data.status === "success") {
                    contactForm.reset();
                }
            } catch (error) {
                console.error("Error:", error);
                formMessage.textContent = "Something went wrong. Please try again later.";
                formMessage.className = "error-msg";
                formMessage.classList.remove("hidden");
            }
        });
    }

    // 4. Mobile Menu Toggle
    const menuToggle = document.querySelector(".menu-toggle");
    const navLinksContainer = document.querySelector(".nav-links");

    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            navLinksContainer.classList.toggle("mobile-active");
            // Basic mobile active styling injected via JS if not in CSS
            if (navLinksContainer.classList.contains("mobile-active")) {
                navLinksContainer.style.display = "flex";
                navLinksContainer.style.flexDirection = "column";
                navLinksContainer.style.position = "absolute";
                navLinksContainer.style.top = "80px";
                navLinksContainer.style.left = "0";
                navLinksContainer.style.width = "100%";
                navLinksContainer.style.background = "rgba(10, 10, 26, 0.95)";
                navLinksContainer.style.padding = "20px";
                navLinksContainer.style.borderBottom = "1px solid rgba(255, 255, 255, 0.1)";
            } else {
                navLinksContainer.style.display = "";
            }
        });
    }
});
