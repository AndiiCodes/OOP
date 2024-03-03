let currentSection = 0;

function next() {
    const sections = document.querySelectorAll('.sec');
    const nextButton = document.querySelector(".next");

    if (currentSection < sections.length - 1) {
        sections[currentSection].classList.remove('active');
        sections[currentSection].classList.add('hidden');
        currentSection++;
        sections[currentSection].classList.remove('hidden');
        sections[currentSection].classList.add('active');
    }
    if (currentSection === sections.length - 1) {
        nextButton.classList.add('hidden');
    }
}
