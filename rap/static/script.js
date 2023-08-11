// alert('asmiya')

// preview image of the profile photo
function displayPreview(event) {
  const previewImage = document.getElementById('imagePreview');
  const photo_label = document.getElementById('photo_label');
  
  const selectedFile = event.target.files[0];

  if (selectedFile) {
      const imageUrl = URL.createObjectURL(selectedFile);
      previewImage.style.backgroundImage = `url(${imageUrl})`;
      photo_label.style.display = 'none';
  } else {
      previewImage.style.backgroundImage = 'none';  // Remove background image
  }
}

document.getElementById('photo').addEventListener('change', displayPreview);

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
const englishLabel_h1 = document.getElementById('english-label-h1');
const nepaliLabel_h1 = document.getElementById('nepali-label-h1');
// console.log("eng_h1", englishLabel_h1);
// console.log("nep_h1", nepaliLabel_h1);

const nepaliLabels = document.querySelectorAll('.nepali-label');
const englishLabels = document.querySelectorAll('.english-label');
// console.log(englishLabels);
// alert("kkk");

languageToggle.addEventListener('change', () => {
    if (languageToggle.checked) {
        englishLabels.forEach(label => label.style.display = 'none');
        nepaliLabels.forEach(label => label.style.display = 'inline');
        englishLabel_h1.style.display = 'none';
        nepaliLabel_h1.style.display = 'block';
    } else {
        englishLabels.forEach(label => label.style.display = 'inline');
        nepaliLabels.forEach(label => label.style.display = 'none');
        nepaliLabel_h1.style.display = 'none';
        englishLabel_h1.style.display = 'block';
      }
});