let data = JSON.parse(jsonData)

function search_animal() {
  let input = document.getElementById('searchbar').value
  input = input.toLowerCase();
  let x = document.querySelector('#list-holder');
  x.innerHTML = ""

  for (i = 0; i < data.length; i++) {
    let obj = data[i];

    if (obj.Name.toLowerCase().includes(input)) {
      const elem = document.createElement("li")
      elem.innerHTML = `${obj.Name} - ${obj.Color}`
      x.appendChild(elem)
    }
  }
}