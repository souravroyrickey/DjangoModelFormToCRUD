$(document).ready(function () {
	var ShowForm = function () {
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$('#modal-task').modal('show');
			},
			success: function (data) {
				$('#modal-task .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm = function () {
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function (data) {
				if (data.form_is_valid) {
					$('#task-table tbody').html(data.task_list);
					$('#modal-task').modal('hide');
				} else {
					$('#modal-task .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

	// create 
	$(".show-form").click(ShowForm);
	$("#modal-task").on("submit", ".create-form", SaveForm);


	//update
	$('#task-table').on("click", ".show-form-update", ShowForm);
	$('#modal-task').on("submit", ".update-form", SaveForm)

	$('#task-table').on("click", ".show-form-detail", ShowForm);

	//delete
	$('#task-table').on("click", ".show-form-delete", ShowForm);
	$('#modal-task').on("submit", ".delete-form", SaveForm)
});