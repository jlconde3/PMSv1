function card_template(wp_code, wp_has_meesage,description,users){
    let users_list = "";
    console.log(users)
    for (i of users){
        users_list = users_list.concat(`<li>${i}</li>`);
    }   

    if (wp_has_meesage){
        const CARD =`
        <a href="">
            <div class="card">
                <div class="wp-section">
                    <div>
                        <p class="wp-title">${wp_code}</p>
                    </div>
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler
                    icon-tabler-message" width="20" height="20" viewBox="0 0 24 24"
                    stroke-width="1" stroke="currentColor" fill="none" stroke-linecap="round"
                    stroke-linejoin="round">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                        <path d="M4 21v-13a3 3 0 0 1 3 -3h10a3 3 0 0 1 3 3v6a3 3 0 0 1 -3 3h-9l-4 4"></path>
                        <line x1="8" y1="9" x2="16" y2="9"></line>
                        <line x1="8" y1="13" x2="14" y2="13"></line>
                    </svg>
                </div>
                <div class="wp-info">
                    <p>${description}</p>
                </div>
        
                <div class="wp-users">
                    <ul>
                        ${users_list}
                    </ul>
                </div>
            </div>
        </a>`

        return CARD
    }

    else {
        const CARD =`
        <a href="">
            <div class="card">
                <div class="wp-section">
                    <div>
                        <p class="wp-title">${wp_code}</p>
                    </div>
                </div>
                <div class="wp-info">
                    <p>${description}</p>
                </div>
        
                <div class="wp-users">
                    <ul>
                        ${users_list}
                    </ul>
                </div>
            </div>
        </a>`
        return CARD
    }
}

function append_card(parent_element,content){
    const container = parent_element;
    let div = document.createElement('div');
    div.innerHTML = content;
    container.appendChild(div);
}


function display_cards(wp_status,wp_code,wp_has_meesage,description,users){

    const to_do = document.getElementById('to-do');
    const in_progress = document.getElementById('in-progress');
    const on_hold = document.getElementById('on-hold')
    const done = document.getElementById('done')
    const cancel = document.getElementById('cancel')

    switch(wp_status){
        case 'TO DO':
            append_card(to_do,card_template(wp_code,wp_has_meesage,description,users));
            break;
        case 'IN PROGRESS':
            append_card(in_progress,card_template(wp_code,wp_has_meesage,description,users));
            break;
        case 'ON HOLD':
            append_card(on_hold,card_template(wp_code,wp_has_meesage,description,users));
            break;
        case 'DONE':
            append_card(done,card_template(wp_code,wp_has_meesage,description,users));
            break;
        case 'CANCEL':
            append_card(cancel,card_template(wp_code,wp_has_meesage,description,users));
            break;
    }
}
document.getElementById('project').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/tools/projects',
        input_id = 'project',
        id_list = [],
        name_list = []
    )
});

document.getElementById('value').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project:document.getElementById('project').value},
        url = '/tools/stations_kanban',
        input_id = 'value',
        id_list = [],
        name_list = []
    )
});


document.getElementById('show_results_button').addEventListener('click',()=>{
    fetch('/kanban/retrive_cards',{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify({
            project:document.getElementById('project').value,
            field:document.getElementById('field').value,
            value:document.getElementById('value').value,
        }),
        headers:{'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then((data) => {
        for (let i in data){
            let j = data[i]
            console.log(j)
            //display_cards(j[0],j[1],false,j[3],j[4])
        }
    });

});
