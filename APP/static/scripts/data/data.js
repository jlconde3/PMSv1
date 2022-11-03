document.getElementById('projects_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('projects_table').setAttribute('style', 'display:block');
});

document.getElementById('actions_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('actions_table').setAttribute('style', 'display:block');
});

document.getElementById('wps_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('wps_table').setAttribute('style', 'display:block');
    fetch('/data/wp', {
        credentials: 'include',
        method: 'GET',
    }).then(response => response.json())
    .then(data => format_data_table('table_wp',data))
});

document.getElementById('users_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('users_table').setAttribute('style', 'display:block');
});



function format_data_table(table_name,data){
    const table = document.getElementById(table_name);
    for (i of data){
        let row = document.createElement('tr')
        for (j of i){
            let td = document.createElement('td');
            td.innerText=j;
            row.appendChild(td);
        }
        table.appendChild(row)
    }
}