const API_URL = "http://127.0.0.1:8000";

async function loadCoffees() {

    const response = await fetch(API_URL + "/coffees");

    const coffees = await response.json();

    const container = document.getElementById("coffeeContainer");

    container.innerHTML = "";

    coffees.forEach(coffee => {

        container.innerHTML += `

        <div class="card">

            <div class="left">

                <img src="${coffee.image}">

                <div class="info">

                    <h2>${coffee.name}</h2>

                    <p>${coffee.description}</p>

                    <div class="vote">

                        ❤️ Votes : ${coffee.votes}

                    </div>

                </div>

            </div>

            <div class="right">

                <button onclick="vote(${coffee.id})">

                    +

                </button>

            </div>

        </div>

        `;

    });

}

async function vote(id){

    await fetch(API_URL + "/vote/" + id,{

        method:"POST"

    });

    loadCoffees();

}

loadCoffees();