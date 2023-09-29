var data = {{ data | tojson | safe }};

// Now you can use 'data' as a JavaScript object
console.log(data);

function submitForm() {
  const data = {
    url: document.getElementById('url').value,
    path: document.getElementById('output-path').value,
    isVideo: document.getElementById('format').value
  };

  fetch('/download', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}