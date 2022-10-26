document.getElementById('submit_button').addEventListener('click',() => {
    let data = {
        project_code: element_id_value('project_code'),
        project_name: element_id_value('project_name'),
        project_client: element_id_value('project_client'),
        project_section: element_id_value('project_section'),
        project_division: element_id_value('project_division'),
        project_budget: element_id_value('project_budget'),
        project_profit_margin: element_id_value('project_profit_margin'),
        project_cpt: element_id_value('project_cpt'),
        project_cpt_actions: element_id_value('project_cpt_actions'),
        project_management_cost: element_id_value('project_management_cost'),
        project_extra_cost: element_id_value('project_extra_cost')
    };

    fetch('/tools/create_project', {
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(window.location.replace("/tools"))
});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools")
});