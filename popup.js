
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("salvar").addEventListener("click", function() {
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.executeScript(
          tabs[0].id,
          {code: "document.documentElement.outerHTML"},
          function(result) {
            console.log(result);
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "http://localhost:8000/salvar_html");
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.onreadystatechange = function() {
              if (xhr.readyState === 4 && xhr.status === 200) {
                document.getElementById("resultado").innerHTML = "HTML salvo com sucesso";
              }
            };
            xhr.send(JSON.stringify({html: result[0]}));
          }
        );
      });
    });
  });
  