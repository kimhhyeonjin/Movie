<template>
  <div>
    <h2>MyProfile</h2>
    <div class="container">
      <div class="image-upload" id="image-upload">
        <form method="post" enctype="multipart/form-data">
          <div class="button">
            <label for="chooseFile">
                👉 CLICK HERE! 👈
            </label>
          </div>
          <input type="file" id="chooseFile" name="chooseFile" accept="image/*" onChange="LoadFile(input)">
        </form>

        <div class="fileContainer">
          <div class="fileInput">
            <p>FILE NAME: </p>
            <p id="fileName"></p>
          </div>
          <div class="buttonContainer">
            <div class="submitButton" id="submitButton">SUBMIT</div>
          </div>
        </div>
      </div>
      
      <div class="image-show" id="image-show"></div>
    </div>

    <!-- <script src="index.js"></script> -->

    <h3>name : {{ username }}</h3>
  </div>
</template>

<script>
export default {
  name: 'MyProfile',
  data() {
    return {
      username: this.$route.params.username
    }
  },
  methods: {
    LoadFile(input) {
      var file = input.files[0];

      var name = document.getElementById('filename');
      name.textContent = file.name;

      var newImage = document.createElement('img');
      newImage.setAttribute('class', 'img');

      newImage.src = URL.createObjectURL(file);

      newImage.style.width = '70%';
      newImage.style.height = '70%';
      newImage.style.visibility = 'hidden';
      newImage.style.objectFit = 'contain';

      var container = document.getElementById('image-show');
      container.appendChild(newImage);
      
      var submit = document.getElementById('submitButton');
      submit.onclick = showImage;     //Submit 버튼 클릭시 이미지 보여주기

        function showImage() {
          var newImage = document.getElementById('image-show').lastElementChild;
          
          //이미지는 화면에 나타나고
          newImage.style.visibility = "visible";
          
          //이미지 업로드 버튼은 숨겨진다
          document.getElementById('image-upload').style.visibility = 'hidden';

          document.getElementById('fileName').textContent = null;     //기존 파일 이름 지우기
        }
    }
  }
}
</script>
<style>

html {
    height: 100%;
}

body {
    font-family: sans-serif;
    height: 100%;
    margin: 0;
}

.container {
    display: flex;
    height: 100%;
    flex-direction: column;
}

.image-upload {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.button {
    display: flex;
    justify-content: center;
}

label {
    cursor: pointer;
    font-size: 1em;
}

#chooseFile {
    visibility: hidden;
}

.fileContainer {
    display: flex;
    justify-content: center;
    align-items: center;
}

.fileInput {
    display: flex;
    align-items: center;
    border-bottom: solid 2px black;
    width: 60%;
    height: 30px;
}

#fileName {
    margin-left: 5px;
}

.buttonContainer {
    width: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 10px;
    background-color: black;
    color: white;
    border-radius: 30px;
    padding: 10px;
    font-size: 0.8em;

    cursor: pointer;
}

.image-show {
    z-index: -1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    width: 100%;
    height: 100%;
}

.img {
    position: absolute;
}

</style>