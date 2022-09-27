const dropArea = document.querySelector(".drag-area"),
  dragText = dropArea.querySelector("header"),
  browseFile = dropArea.querySelector("#browseFile"),
  input = dropArea.querySelector("#diseaseImage"),
  form = document.querySelector("#form"),
  cancel = document.querySelector("#Cancel");

let file;
const initialHTML = dropArea.innerHTML;
browseFile.onclick = () => {
  input.click();
};

input.addEventListener("change", function () {
  file = this.files[0];
  dropArea.classList.add("active");
  showFile();
});

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
  dragText.textContent = "Drag & Drop to Upload File";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  file = event.dataTransfer.files[0];
  showFile();
});

const showFile = () => {
  let fileType = file.type;
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"];
  if (validExtensions.includes(fileType)) {
    // let fileReader = new FileReader();
    // fileReader.onload = () => {
    //   let fileURL = fileReader.result;
    //   let imgTag = `<img src="${fileURL}" alt="image" id="uploaded-image">`;
    //   dropArea.innerHTML = imgTag;
    // };
    // fileReader.readAsDataURL(file);
  } else {
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
};

cancel.addEventListener("click", (e) => {
  e.preventDefault();
  dropArea.innerHTML = initialHTML;
});

// form.addEventListener("submit", (e) => {});
