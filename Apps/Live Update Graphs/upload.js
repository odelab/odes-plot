// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
  // Great success! All the File APIs are supported.
} else {
  alert('The File APIs are not fully supported in this browser.');
}

// choose a single file to upload, then return the FileReader object
function handleSingleFileSelect(evt, editor) {
    var file = evt.target.files[0]; // first of the FileList object

    if (file) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
	      editor.setValue(contents)
        alert( "Got data file.\n" 
              +"name: " + file.name + "\n"
              +"type: " + file.type + "\n"
              +"size: " + file.size + " bytes\n"
              + "starts with: " + contents.substr(1, contents.indexOf("\n"))
        );  
      }

      // asynchronous readAsText, need onload callback to see the result
      r.readAsText(file);
      
    } else { 
      alert("Failed to load file");
      return null;
    }
}

// handle data
function handleDataFileSelect(evt, editor) {
    var file = evt.target.files[0]; // first of the FileList object

    if (file) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
	      editor.setValue(contents)
        alert( "Got data file.\n" 
              +"name: " + file.name + "\n"
              +"type: " + file.type + "\n"
              +"size: " + file.size + " bytes\n"
              + "starts with: " + contents.substr(1, contents.indexOf("\n"))
        );  
      }

      // asynchronous readAsText, need onload callback to see the result
      r.readAsText(file);
      
    } else { 
      alert("Failed to load file");
      return null;
    }
}

// trigger
// document.getElementById('dataFile').addEventListener('change', handleSingleFileSelect, false);