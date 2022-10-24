document.getElementById('projects_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('projects_table').setAttribute('style', 'display:block');
    create_table("projects")
});

document.getElementById('actions_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('actions_table').setAttribute('style', 'display:block');
});

document.getElementById('wps_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('wps_table').setAttribute('style', 'display:block');
});

document.getElementById('users_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('users_table').setAttribute('style', 'display:block');
});

document.getElementById('users_activity_table_button').addEventListener('click',()=>{
    hide_table()
    document.getElementById('users_activity_table').setAttribute('style', 'display:block');
});

