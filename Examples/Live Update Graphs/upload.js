function handleSingleFileSelect(evt) {
    var files = evt.target.files[0]; // first of the FileList object

    if (f) {
      var r = new FileReader();
      r.onload = function(e) { 
	      var contents = e.target.result;
        alert( "Got data file.\n" 
              +"name: " + f.name + "\n"
              +"type: " + f.type + "\n"
              +"size: " + f.size + " bytesn"
              + "starts with: " + contents.substr(1, contents.indexOf("\n"))
        );  
      }
      r.readAsText(f);
    } else { 
      alert("Failed to load file");
    }

    }
  }

  document.getElementById('dataFile').addEventListener('change', handleSingleFileSelect, false);