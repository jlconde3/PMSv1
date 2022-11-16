let j = 1;

document.getElementById('project').addEventListener('click',()=>{
    retrive_data_actions(
        data = {},
        url = '/tools/projects',
        input_id = 'project',
        id_list = [],
        name_list = []
    )
});

document.getElementById('action').addEventListener('click',()=>{
    retrive_data_actions(
        data = {project:document.getElementById('project').value,},
        url = '/tools/actions',
        input_id = 'action',
        id_list = [],
        name_list = []
    )
});

document.getElementById('retrive_button').addEventListener('click',()=>{
    const project = document.getElementById('project').value;
    const action = document.getElementById('action').value;

    if (!isEmpty(action)){
        fetch('/actions/retrive_action',{
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify({project:project,action:action}),
            headers:{'Content-Type': 'application/json'}
        })
        .then(response => response.json())
        .then(data => {
            display_data_project(data['response'])
        })
    }
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

function display_data_project (response){
    document.getElementById('client').value = response[0];
    document.getElementById('phase').value = response[3];
    document.getElementById('date').value = get_date(response[6]);
    document.getElementById('discipline').value = response[2];
    document.getElementById('system').value = response[5];
    document.getElementById('type').value = response[1];
    document.getElementById('description').value = response[4];
}