let j = 1;
let q = 1;

let projects = true;
let disciplines = true;
let phases = true;
let zones = true;
let types = true;
let stations = true;


let action_area_task ={
    'actions_0':true,
    'areas_0': true,
    'tasks_0':true,
    'users_0':true,
};

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data(
        reload = projects,
        data = {},
        url = '/tools/projects',
        input_id = 'project_code',
    )
    projects = false;
});

document.getElementById('discipline_code').addEventListener('click',()=>{
    retrive_data(
        reload = disciplines,
        data = {'project_code': document.getElementById('project_code').value},
        url = '/tools/disciplines',
        input_id = 'discipline_code',
    )
    disciplines = false;   
});

document.getElementById('phase_code').addEventListener('click',()=>{
    retrive_data(
        reload = phases,
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value
        },
        url = '/tools/phases',
        input_id = 'phase_code',
    )
    phases = false;   
});

document.getElementById('wp_zone').addEventListener('click',()=>{
    retrive_data(
        reload = zones,
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value
        },
        url = '/tools/zones',
        input_id = 'wp_zone',
    )
    zones = false;   
});

document.getElementById('wp_type').addEventListener('click',()=>{
    retrive_data(
        reload = types,
        data = {'project_code': document.getElementById('project_code').value},
        url = '/tools/types',
        input_id = 'wp_type',
    )
    types = false;   
});

document.getElementById('wp_station').addEventListener('click',()=>{
    retrive_data(
        reload = stations,
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value,
            'zone_code':document.getElementById('wp_zone').value
        },
        url = '/tools/stations',
        input_id = 'wp_station',
    )
    stations = false;   
});

document.getElementById(`action_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`actions_0`],
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value,
            'zone_code':document.getElementById('wp_zone').value
        },
        url = '/tools/actions',
        input_id = `action_0`,
    )
    action_area_task[`actions_0`] = false;
})


document.getElementById(`area_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`areas_0`],
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value,
            'zone_code':document.getElementById('wp_zone').value
        },
        url = '/tools/areas',
        input_id = `area_0`,
    )
    action_area_task[`areas_0`] = false;
})

document.getElementById(`task_0`).addEventListener('click',()=>{
    retrive_data(
        reload = action_area_task[`tasks_0`],
        data = {
            'project_code': document.getElementById('project_code').value,
            'discipline_code': document.getElementById('discipline_code').value,
            'phase_code':document.getElementById('phase_code').value,
            'station_code':document.getElementById('wp_station').value
        },
        url = '/tools/tasks',
        input_id = `task_0`,
    )
    action_area_task[`tasks_0`] = false;
})


document.getElementById('more_button').addEventListener('click',() => {
    let i = j;
    action_area_task[`actions_${i}`] = true;
    action_area_task[`areas_${i}`] = true;
    action_area_task[`tasks_${i}`] = true;

    add_more('subtasks',
    `
    <div>
        <label class = "label-title">Task</label>
    </div>
    <div class="fields-group">
    <div>
        <label class = "label-field">Action</label><br>
        <input class = "input-3" name = "task_action" id="action_${i}">
        <datalist id="actions_${i}" class = "input-3" ></datalist>
    </div>
    <div>
        <label class = "label-field">Area</label><br>
        <input class = "input-3" type="text" name = "task_area" id="area_${i}">
        <datalist id="areas_${i}" class = "input-3"></datalist>
    </div>
    <div>
        <label class = "label-field">Task</label><br>
        <input class = "input-3" name = "task_code" id="task_${i}">
        <datalist id="tasks_${i}" class = "input-3"></datalist>
    </div>
    </div>
    `);

    document.getElementById(`action_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`actions_${i}`],
            data = {
                'project_code': document.getElementById('project_code').value,
                'discipline_code': document.getElementById('discipline_code').value,
                'phase_code':document.getElementById('phase_code').value,
                'zone_code':document.getElementById('wp_zone').value
            },
            url = '/tools/actions',
            input_id = `action_${i}`,
        )
        action_area_task[`actions_${i}`] = false;

    });

    document.getElementById(`area_${j}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`areas_${i}`],
            data = {
                'project_code': document.getElementById('project_code').value,
                'discipline_code': document.getElementById('discipline_code').value,
                'phase_code':document.getElementById('phase_code').value,
                'zone_code':document.getElementById('wp_zone').value
            },
            url = '/tools/areas',
            input_id = `area_${i}`,
        )
        action_area_task[`areas_${i}`] = false;
    });

    document.getElementById(`task_${i}`).addEventListener('click',()=>{
        retrive_data(
            reload = action_area_task[`tasks_${i}`],
            data = {
                'project_code': document.getElementById('project_code').value,
                'discipline_code': document.getElementById('discipline_code').value,
                'phase_code':document.getElementById('phase_code').value,
                'station_code':document.getElementById('wp_station').value
            },
            url = '/tools/tasks',
            input_id = `task_${i}`,
        )
        action_area_task[`tasks_${i}`] = false;
    });
    j++;
});

const validate_window = `

<div class="top-buttons">
    <button class = "black-button" type="button" id="validate_button" >Validate WP</button>
    <button class = "white-button" type="button" id="cancel_validate_button" >Cancel</button>
</div>
<form autocomplete="off" method="post">
    <div class="border"></div>
        <div class="group">
            <div>
                <label class = "label-title">WP</label>
            </div>
            <div class="fields-group">
                <div>
                    <label class = "label-field">Code</label><br>
                    <input id = "wp_code" class="input-2" type="text">
                </div>
            </div>
        </div>
        <div class="border"></div>
        <div class="group">
            <div>
                <label class = "label-title">Attributes</label>
            </div>
            <div class="fields-group">
                <div>
                    <label class = "label-field">Difficulty</label><br>
                    <input type="number" id = "wp_difficulty">
                </div>
                <div>
                    <label class = "label-field">Volume</label><br>
                    <input type="number" id = "wp_volume">
                </div>
                <div>
                    <label class = "label-field">Complexity</label><br>
                    <input type="number" id = "wp_complexity">
                </div>
            </div>
        </div>
        <div class="group">
            <div>
                <label class = "label-title">Time</label>
            </div>
            <div class="fields-group">
                <div>
                    <label class = "label-field">Contracted</label><br>
                    <input type="number" id = "wp_contracted_time">
                </div>
                <div>
                    <label class = "label-field">Planned</label><br>
                    <input type="number" id = "wp_planned_time">
                </div>
                <div>
                    <label class = "label-field">Scheduled</label><br>
                    <input type="number" id = "wp_scheduled_time">
                </div>
            </div>
        </div>
        <div class="border"></div>
        <div id = "users">
            <div class="group">
                <div>
                    <label class = "label-title">In charge</label>
                </div>
                <div class="fields-group">
                    <div>
                        <label class = "label-field">User</label><br>
                        <input type="text" name = "username" id="user_0">
                        <datalist class = "input-4" id="users_0" ></datalist>
                    </div>
                    <div>
                        <label class = "label-field">Level</label><br>
                        <input type="number" name = "user_level" id ="user_level_0">
                    </div>
                </div>
            </div>
    
        </div>
        <div class="group">
            <button type="button" id = "more_users_button" class="more-tasks">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-circle-plus"
                width="40" height="40" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor"
                fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <circle cx="12" cy="12" r="9"></circle>
                    <line x1="9" y1="12" x2="15" y2="12"></line>
                    <line x1="12" y1="9" x2="12" y2="15"></line>
                </svg>
                <p>Click here to add more resources...</p>
            </button>
        </div>
    </div>
</form>
`
document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('submit_button').addEventListener('click',() => {
    let i = 0;
    let empty = false;
    const inputs = document.getElementsByTagName('input');

    for (input of inputs){
        if (input.value.replace(/ /g,'') == ""){
            input.style.border = "red solid 1px";
            empty = true;
        }
        else{
            input.style.border = "#EAEAEA solid 1px";
        }
        i++;
    }    

    if (!empty){
        add_validate_window('validate_window',validate_window);
        let data = {
            project: document.getElementById('project_code').value,
            discipline: document.getElementById('discipline_code').value,
            phase: document.getElementById('phase_code').value,
            zone: document.getElementById('wp_zone').value,
            type: document.getElementById('wp_type').value,
            station:document.getElementById('wp_station').value,
            actions:element_name_value('task_action'),
            areas:element_name_value('task_area'),
            tasks:element_name_value('task_code'),
        };
        fetch("/tools/generate_wp",{
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json'
            }
            }
        ).then((response) => response.json()
        ).then((data) => {
            document.getElementById('validate_window').showModal()
            document.getElementById('wp_code').value = data.wp_code;
            document.getElementById('wp_difficulty').value = data.wp_dif;
            document.getElementById('wp_volume').value = data.wp_vol;
            document.getElementById('wp_complexity').value = data.wp_cpl;
            document.getElementById('wp_contracted_time').value = data.wp_contracted_time;
            document.getElementById('wp_planned_time').value = data.wp_planned_time;
            }
        ).then(
            document.getElementById(`user_0`).addEventListener('click',()=>{
                retrive_data(
                    reload = action_area_task[`users_0`],
                    data = {
                        'project_code': document.getElementById('project_code').value
                    },
                    url = '/tools/users_projects',
                    input_id = `user_0`,
                )
                action_area_task[`users_0`] = false;
            })

        ).then(
            document.getElementById(`user_level_0`).addEventListener('click',()=>{
                console.log('ahora')
                data = {
                    project: document.getElementById('project_code').value,
                    user: document.getElementById('user_0').value,
                    tasks:element_name_value('task_code')
                }

                fetch("/tools/user_level",{
                    credentials: 'include',
                    method: 'POST',
                    body: JSON.stringify(data),
                    headers:{
                        'Content-Type': 'application/json'
                    }
                    }
                ).then( response => response.json()
                ).then(data => document.getElementById(`user_level_0`).value = data.level)    
            })

        ).then(
            document.getElementById('more_users_button').addEventListener('click',() => {
                let k = q;
                action_area_task[`users_${k}`] = true;
                add_more('users',
                `
                <div>
                    <label class = "label-title">In charge</label>
                </div>
                <div class="fields-group">
                    <div>
                        <label class = "label-field">User</label><br>
                        <input type="text" name = "username" id = "user_${k}">
                        <datalist class = "input-4" id="users_${k}" ></datalist>
                    </div>
                    <div>
                        <label class = "label-field">Level</label><br>
                        <input type="number" name = "user_level" id = "user_level_${k}">
                    </div>
                </div>
                `);
            
                document.getElementById(`user_${k}`).addEventListener('click',()=>{
                    retrive_data(
                        reload = action_area_task[`users_${k}`],
                        data = {
                            'project_code': document.getElementById('project_code').value,
                        },
                        url = '/tools/users_projects',
                        input_id = `user_${k}`,
                    )
                    action_area_task[`users_${k}`] = false;
                });
                q++;

                document.getElementById(`user_level_${k}`).addEventListener('click',()=>{
                    console.log('ahora')
                    data = {
                        project: document.getElementById('project_code').value,
                        user: document.getElementById(`user_${k}`).value,
                        tasks:element_name_value('task_code')
                    }
    
                    fetch("/tools/user_level",{
                        credentials: 'include',
                        method: 'POST',
                        body: JSON.stringify(data),
                        headers:{
                            'Content-Type': 'application/json'
                        }
                        }
                    ).then( response => response.json()
                    ).then(data => document.getElementById(`user_level_${k}`).value = data.level)    
                });
            })
        ).then(
            document.getElementById('cancel_validate_button').addEventListener('click',() => {
                delete_childs('validate_window')
                document.getElementById('validate_window').close(); 
            })
        ).finally(
            document.getElementById('validate_button').addEventListener('click',() => {
                let i = 0;
                let empty = true;
                const inputs = document.getElementsByTagName('input');
                
                for (input of inputs){
                    if (input.value.replace(/ /g,'') == ""){
                        input.style.border = "red solid 1px";
                        empty = true;
                    }
                    else{
                        empty = false;
                        input.style.border = "#EAEAEA solid 1px";
                    }
                    i++;
                }    
                if (!empty){        
                    let data = {
                        project_code: element_id_value('project_code'),
                        discipline_code: element_id_value('discipline_code'),
                        phase_code: element_id_value('phase_code'),
                        wp_type: element_id_value('wp_station'),
                        wp_station: element_id_value('wp_station'),
                        wp_zone: element_id_value('wp_zone'),
                        task_action: element_name_value('task_action'),
                        task_area: element_name_value('task_area'),
                        task_code: element_name_value('task_code'),
                        wp_code: element_id_value('wp_code'),
                        wp_difficulty: element_id_value('wp_difficulty'),
                        wp_volume: element_id_value('wp_volume'),
                        wp_complexity: element_id_value('wp_complexity'),
                        wp_contracted_time: element_id_value('wp_contracted_time'),
                        wp_planned_time: element_id_value('wp_planned_time'),
                        wp_scheduled_time:  element_id_value('wp_scheduled_time'),
                        username: element_name_value('username'),
                        user_level: element_name_value('user_level')
                    };
            
                    fetch('/tools/create_action', {
                        credentials: 'include',
                        method: 'POST',
                        body: JSON.stringify(data),
                        headers:{
                            'Content-Type': 'application/json'
                        }
                    }).then(window.location.replace("/tools"))
                }
                else{
                    alert("You left some fields empty!!")
                }
            })
        )
    }
    else{
        alert("You left some fields empty!!")
    }
});