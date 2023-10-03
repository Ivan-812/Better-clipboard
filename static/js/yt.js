// Now you can use 'data' as a JavaScript object
console.log(data);

document.getElementById('output-path').value = data['outputPath']
document.getElementById('format').value = data.format

function submitForm() {
  const data = {
    url: document.getElementById('url').value,
    path: document.getElementById('output-path').value,
    format: document.getElementById('format').value
  };

  fetch('/download', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}