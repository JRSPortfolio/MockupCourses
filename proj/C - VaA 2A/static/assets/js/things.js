window.addEventListener('load', getEntryData)

function getEntryData(){
    document.getElementById("entrar").addEventListener('click', function(){
        const entryData = {
        email : document.getElementById('email').value,
        password : document.getElementById('password').value
        };
        getJSON(`${URL}/login}`, entryData);
    })
    
}

function getJSON(URL, data, mode = 'cors'){
    fetch(URL,{
        method: 'GET',
        mode: mode,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
}
