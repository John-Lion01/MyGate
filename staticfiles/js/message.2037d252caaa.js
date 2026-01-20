const form = document.querySelector("#contact form")

form.addEventListener("submit", function(e){
    e.preventDefault();
    const formData = new FormData(this);
    const url = "/fr/message/api";
    var pop = document.createElement("li")
    // console.log("before fectch")
    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error("Server Error");
        return response.json()
    })
    .then(data => {
        // console.log(data)
        if (data.status == "success") {
            pop.classList.add("success");
            pop.textContent = data["message"];
            // console.log(data.message)
            form.reset();
        } else {
            pop.classList.add("error");
            pop.textContent = data["message"];
        }
    })
    .catch(error => {
        pop.classList.add("error");
        pop.textContent = "Error : Try again later please !";
    })

    const popup = document.querySelector("div.popup ul");
    popup.textContent = "";
    popup.appendChild(pop)
    setTimeout(() => {
        popup.textContent = "";
    }, 10000);
    
});