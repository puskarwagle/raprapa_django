// preview image of the profile photo
function handleImagePreview(event) {
  const fileInput = event.target;
  const imagePreview = document.getElementById('imagePreview');
  if (fileInput.files && fileInput.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      imagePreview.innerHTML = `<img src="${e.target.result}" style="max-width: 100%; max-height: 100%;">`;
    };
    reader.readAsDataURL(fileInput.files[0]);
  } else {
    imagePreview.innerHTML = 'फोटो';
  }
}
document.getElementById('photo').addEventListener('change', handleImagePreview);

// Default email address
function emaildefault() {
  document.getElementById("email").defaultValue = 'sulav0902@gmail.com';
}
emaildefault();

// Update name value
function updateNamePlaceholder() {
  const nameInput = document.getElementById('name');
  const namePlaceholder = document.getElementById('nameValue');
  const name = nameInput.value;
  namePlaceholder.textContent = name;
}

const languageToggle = document.getElementById('language-toggle');
console.log("lang", languageToggle);
const languageImage = document.getElementById('languageImage');
function toggleLanguage() {
  if (languageToggle.checked) {
    document.querySelector(".english-version").style.display = "block";
    document.querySelector(".nepali-version").style.display = "none";
    languageImage.src = './images/english.png';
  } else {
    document.querySelector(".english-version").style.display = "none";
    document.querySelector(".nepali-version").style.display = "block";
    languageImage.src = './images/nepal.png';
  }
}
languageToggle.addEventListener('change', toggleLanguage);