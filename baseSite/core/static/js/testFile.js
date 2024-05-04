async function getMealNames(){
    let tmp = await fetch("http://127.0.0.1:8000/mealsNames");
    let data = await tmp.json()
    console.log(data.names);

    // fetch('http://127.0.0.1:8000/mealsNames')
    // .then((response) => {
    //     for (var pair of response.headers.entries()) {
    //     console.log(pair[0]+ ': '+ pair[1]);
    //     }
    // });

}