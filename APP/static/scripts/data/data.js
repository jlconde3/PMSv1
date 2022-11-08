document.getElementById('projects_table_button').addEventListener('click',()=>{
    hide_table()
    delete_childs('actions_table')
    display_table('project','projects_table',[1,2])
    document.getElementById('projects_table').setAttribute('style', 'display:block');
});

document.getElementById('actions_table_button').addEventListener('click',()=>{
    hide_table()
    delete_childs('actions_table')
    display_table('action','actions_table',[1,2])
    document.getElementById('actions_table').setAttribute('style', 'display:block');
});

document.getElementById('wps_table_button').addEventListener('click',()=>{
    hide_table()
    display_table('wp','wps_table',["Project","Code","Status","Scheduled time","User",""])
    document.getElementById('wps_table').setAttribute('style', 'display:block');
});

document.getElementById('users_table_button').addEventListener('click',()=>{
    delete_childs('users_table')
    hide_table()
    display_table('user','user_table',[1,2])
    document.getElementById('users_table').setAttribute('style', 'display:block');
});


function display_table (url,table_name,headers){

    fetch(`/data/${url}`, {
        credentials: 'include',
        method: 'GET',
    })
    .then(response => response.json())
    .then((data) => {

        const table = document.getElementById(table_name);

        let row = document.createElement('tr')

        for (i of headers){
            let th = document.createElement('th');
            th.innerText=i;
            row.appendChild(th);
        }
        table.appendChild(row)

        for (i of data){
            let row = document.createElement('tr')
            for (j of i){
                let td = document.createElement('td');
                td.innerText=j;
                row.appendChild(td);
            }
            button = document.createElement('button')
            button.setAttribute('class','tools-button')
            button.setAttribute('class','info-button')
            button.setAttribute('id',`row_${i[1]}`)
            button.setAttribute('name','info_button')
            button.innerHTML = `
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-info-circle"
                    width="40" height="40" viewBox="0 0 24 24" stroke-width="0.5"
                    stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <circle cx="12" cy="12" r="9"></circle>
                    <line x1="12" y1="8" x2="12.01" y2="8"></line>
                    <polyline points="11 12 12 12 12 16 13 16"></polyline>
                </svg>
            `
            row.appendChild(button);
            table.appendChild(row)
        }

        buttons = [...document.getElementsByName('info_button')]
        buttons.forEach((item)=>{
            item.addEventListener('click',()=>{
                fetch('/data/info_wp', {
                    credentials: 'include',
                    method: 'GET',
                }).then(response => response.json())
                .then((data) =>{})
            })
        })
    })
}
