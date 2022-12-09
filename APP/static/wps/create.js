let j = 1;
let q = 1;

document.getElementById('project_code').addEventListener('click',()=>{
    retrive_data(
        data = {},
        url = '/data/projects',
        input_id = 'project_code',
        id_list = ['phase_code','system_code','zone_code','discipline_code','line_code','station_code'],
        name_list = ['task_action','task_area','task_code']
    )
});
document.getElementById('phase_code').addEventListener('click',()=>{
    retrive_data(
        data = {
            project: document.getElementById('project_code').value,
            discipline: document.getElementById('discipline_code').value
        },
        url = '/data/phases',
        input_id = 'phase_code',
        id_list = ['system_code','zone_code'],
        name_list = ['task_action','task_area','task_code']
    )
});

document.getElementById('system_code').addEventListener('click',()=>{
    retrive_data(
        data = {
            project: document.getElementById('project_code').value,
            phase:document.getElementById('phase_code').value,
        },
        url = '/data/systems',
        input_id = 'system_code',
        id_list = ['zone_code'],
        name_list = ['task_action','task_area','task_code']
    )
});

document.getElementById('zone_code').addEventListener('click',()=>{
    retrive_data(
        data = {
            project: document.getElementById('project_code').value,
            phase:document.getElementById('phase_code').value,
            system: document.getElementById('system_code').value,
        },
        url = '/data/zones',
        input_id = 'zone_code',
        id_list = [],
        name_list = ['task_action','task_area','task_code']
    )
});

document.getElementById('discipline_code').addEventListener('click',()=>{
    retrive_data(
        data = {project: document.getElementById('project_code').value},
        url = '/data/disciplines',
        input_id = 'discipline_code',
        id_list = ['line_code','station_code'],
        name_list = ['task_action','task_area','task_code']
    )
});

document.getElementById('line_code').addEventListener('click', async ()=>{
    await retrive_data(
        data = {
        project: document.getElementById('project_code').value,
        discipline: document.getElementById('discipline_code').value,
        },
        url = '/data/lines',
        input_id = 'line_code',
        id_list = ['station_code'],
        name_list = ['task_action','task_area','task_code']
    )
    await disabled_fields()
});

document.getElementById('station_code').addEventListener('click',()=>{
    retrive_data(
        data = {
            project: document.getElementById('project_code').value,
            discipline: document.getElementById('discipline_code').value,
            line: document.getElementById('line_code').value
        },
        url = '/data/stations',
        input_id ="station_code",
        id_list = [],
        name_list = ['task_action','task_area','task_code']
    )
});


document.getElementById(`action_0`).addEventListener('click', async ()=>{
    retrive_data(
        data = {
            project:document.getElementById('project_code').value,
            phase:document.getElementById('phase_code').value,
            system:document.getElementById('system_code').value,
            zone:document.getElementById('zone_code').value,
            discipline: document.getElementById('discipline_code').value,
            station:document.getElementById('station_code').value
        },
        url = '/data/actions',
        input_id = `action_0`,
        id_list = [],
        name_list = ['task_area_0','task_code_0']
    )
})

document.getElementById(`area_0`).addEventListener('click',()=>{
    retrive_data(
        data = {
            project:document.getElementById('project_code').value,
            phase:document.getElementById('phase_code').value,
            system:document.getElementById('system_code').value,
            zone:document.getElementById('zone_code').value
        },
        url = '/data/areas',
        input_id = `area_0`,
        id_list = [],
        name_list = []
    )
})

document.getElementById(`task_0`).addEventListener('click',()=>{
    retrive_data(
        data = {
            project: document.getElementById('project_code').value,
            discipline: document.getElementById('discipline_code').value,
            line: document.getElementById('line_code').value,
            station:document.getElementById('station_code').value
        },
        url = '/data/tasks',
        input_id = `task_0`,
        id_list = [],
        name_list = []
    )
})

document.getElementById('more_button').addEventListener('click',() => {
    let i = j;

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
            data = {
                project:document.getElementById('project_code').value,
                phase:document.getElementById('phase_code').value,
                system:document.getElementById('system_code').value,
                zone:document.getElementById('zone_code').value,
                discipline: document.getElementById('discipline_code').value,
                station:document.getElementById('station_code').value
            },
            url = '/data/actions',
            input_id = `action_${i}`,
            id_list = [],
            name_list = [`task_area_${i}`,`task_code_${i}`]
        )
    });
    
    document.getElementById(`area_${i}`).addEventListener('click',()=>{
        retrive_data(
            data = {
                project:document.getElementById('project_code').value,
                discipline:document.getElementById('discipline_code').value,
                phase:document.getElementById('phase_code').value,
                zone:document.getElementById('zone_code').value
            },
            url = '/data/areas',
            input_id = `area_${i}`,
            id_list = [],
            name_list = []
        )
    });

    document.getElementById(`task_${i}`).addEventListener('click',()=>{
        retrive_data(
            data = {
                project: document.getElementById('project_code').value,
                discipline: document.getElementById('discipline_code').value,
                line: document.getElementById('line_code').value,
                station:document.getElementById('station_code').value
            },
            url = '/data/tasks',
            input_id = `task_${i}`,
            id_list = [],
            name_list = []
        )
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
            if (input.disabled == false){
                input.style.border = "red solid 1px";
                empty = true;
            }
        }
        else{
            input.style.border = "#EAEAEA solid 1px";
        }
        i++;
    }    

    if (!empty){
        let data = {
            project: document.getElementById('project_code').value,
            discipline: document.getElementById('discipline_code').value,
            phase: document.getElementById('phase_code').value,
            zone: document.getElementById('zone_code').value,
            wp_line: document.getElementById('line_code').value,
            station:document.getElementById('station_code').value,
            actions:element_name_value('task_action'),
            areas:element_name_value('task_area'),
            tasks:element_name_value('task_code'),
        };
        fetch("/data/generate_wp",{
            credentials: 'include',
            method: 'POST',
            body: JSON.stringify(data),
            headers:{
                'Content-Type': 'application/json'}
            }
        ).then(response => {
            if (response.status == 212 ){
                response.json().then(data => 
                    {alert('This combination has been created previously:'+ `${data.area}-${data.task}`)}
            )}
            else if(response.status == 213){
                response.json().then(data => {
                    add_validate_window('validate_window',validate_window)
                    document.getElementById('validate_window').showModal();
                    document.getElementById('wp_code').value = data.wp_code;
                    document.getElementById('wp_difficulty').value = data.wp_dif;
                    document.getElementById('wp_volume').value = data.wp_vol;
                    document.getElementById('wp_complexity').value = data.wp_cpl;
                    document.getElementById('wp_contracted_time').value = data.wp_contracted_time;
                    document.getElementById('wp_planned_time').value = data.wp_planned_time;
                    document.getElementById(`user_0`).addEventListener('click',()=>{
                        retrive_data(
                            data = {
                                'project_code': document.getElementById('project_code').value
                            },
                            url = '/data/users_projects',
                            input_id = `user_0`,
                            id_list = ['user_level_0'],
                            name_list = []
                        )
                    })
                    
                    document.getElementById(`user_level_0`).addEventListener('click',()=>{
                        data = {
                            project: document.getElementById('project_code').value,
                            user: document.getElementById('user_0').value,
                            tasks:element_name_value('task_code')
                        }
                        fetch("/data/user_level",{
                            credentials: 'include',
                            method: 'POST',
                            body: JSON.stringify(data),
                            headers:{
                                'Content-Type': 'application/json'
                            }
                        }).then( response => response.json()
                        ).then(data => document.getElementById(`user_level_0`).value = data.level)    
                    })
                    
                    document.getElementById('more_users_button').addEventListener('click',() => {
                        let k = q;
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
                                data = {
                                    'project_code': document.getElementById('project_code').value,
                                },
                                url = '/data/users_projects',
                                input_id = `user_${k}`,
                                id_list = [`user_level_${k}`],
                                name_list = []
                                
                            )
                        });
                        q++
                        document.getElementById(`user_level_${k}`).addEventListener('click',()=>{
                            data = {
                                project: document.getElementById('project_code').value,
                                user: document.getElementById(`user_${k}`).value,
                                tasks:element_name_value('task_code')
                            }
                            fetch("/data/user_level",{
                                credentials: 'include',
                                method: 'POST',
                                body: JSON.stringify(data),
                                headers:{
                                    'Content-Type': 'application/json'
                                }
                            }).then( response => response.json()
                            ).then(data => document.getElementById(`user_level_${k}`).value = data.level)    
                        });
                    })
                    
                    document.getElementById('cancel_validate_button').addEventListener('click',() => {
                        reset_users_wp(j)
                    })

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
                                wp_line: element_id_value('line_code'),
                                station_code: element_id_value('station_code'),
                                wp_zone: element_id_value('zone_code'),
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
                    
                            fetch('/data/validate_wp', {
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
                }
            )}
        })
    }
    else{
        alert("You left some fields empty!!")
    }
});

function disabled_fields(){
    if (document.getElementById('line_code').value == 'DESIGN'){
        for (i of document.getElementsByName('task_area')){
            i.disabled = false;
        }
        for (i of document.getElementsByName('task_action')){
            i.disabled = true;
        }
    }
    else{
        for (i of document.getElementsByName('task_area')){
            i.disabled = true;
        }
        for (i of document.getElementsByName('task_action')){
            i.disabled = false;
        }
    }
}

