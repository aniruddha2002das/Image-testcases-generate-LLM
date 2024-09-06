async function generateTestCases() {
  const context = document.getElementById("context").value;
  const files = document.getElementById("screenshotUpload").files;

  const formData = new FormData();
  formData.append("context", context);

  for (let i = 0; i < files.length; i++) {
    formData.append("screenshots", files[i]);
  }

  const response = await fetch("/generate-test-cases", {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  document.getElementById("output").innerText = JSON.stringify(data, null, 2);
}
