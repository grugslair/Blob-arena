mergeInto(LibraryManager.library, {

  
  // this write to the data storage
  SaveToLocalStorage: function(key, value) {
    key = UTF8ToString(key);
    value = UTF8ToString(value);
    localStorage.setItem(key, value);
  },

    getAllData:  function() {
      let items = [];
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        const value = localStorage.getItem(key);
        items.push({ [key]: value });
      }
      
      var createdJson = JSON.stringify(items);
      console.log("this is form the jsend");
      console.log(createdJson);

      gameInstance.SendMessage(
            "WorldManager",
            "ReturnFromTheJsEnd",
            createdJson
          );

    },


    ClearAllLocalData:  function() {
      localStorage.clear();
    },
  
  CopyToClipboardImpl: function(textPointer) {
        var text = UTF8ToString(textPointer);
        navigator.clipboard.writeText(text).then(function() {
        console.log('Async: Copying to clipboard was successful!');
        }, function(err) {
        console.error('Async: Could not copy text: ', err);
        });
    },

  PedersenFunction: function(value1Ptr,value2Ptr) {
    
      const hash = window.customStark.ec.starkCurve.pedersen(BigInt(value1Ptr), BigInt(value2Ptr));
      console.log("js Side");
      console.log("pedersan hash: " + hash);


      // var numberAsString = BigInt(hash).toString();
      // console.log("into big int : " + numberAsString);


      var buffer = _malloc(lengthBytesUTF8(hash) + 1);
      writeStringToMemory(hash, buffer);
      return buffer;
	}
});