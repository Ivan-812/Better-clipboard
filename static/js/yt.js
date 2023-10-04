// Now you can use 'data' as a JavaScript object
//console.log(data);

// ----- on load -----
$('#output-path').val(data['outputPath']);
$('#format').val(data.format);
$('#custom-filename').val(data.customFilename)
$('#custom-filename-switch').prop('checked', data.customFilenameSwitch);
//$('.overlay').hide();

// ----- switch -----
var switchElement = document.getElementById('custom-filename-switch');
var inputElement = document.getElementById('custom-filename');
inputElement.disabled = true

// Add an event listener for the switch
switchElement.addEventListener('change', function() {
    if (this.checked) {
        inputElement.disabled = false;
    } else {
        inputElement.disabled = true;
    }
});

// ----- POST Request -----
function submitForm() {
  const innerData = {
    url: $('#url').val(),
    outputPath: $('#output-path').val(),
    format: $('#format').val(),
    customFilename: $('#custom-filename').val(),
    customFilenameSwitch: $('#custom-filename-switch').prop('checked')
  };

  fetch('/download', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(innerData)
  });
}