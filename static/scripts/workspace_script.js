$(document).ready(function () {
    // Function to show/hide the workspace creation form
    $("#toggleCreateFormBtn").click(function () {
        $("#createWorkspaceFormContainer").toggle();
    });

    // Function to submit the workspace creation form using Ajax
    $("#createWorkspaceForm").submit(function (event) {
        event.preventDefault();
        const form = $(this);
        $.ajax({
            url: "{% url 'create_workspace' %}",
            type: "post",
            data: new FormData(this),
            processData: false,
            contentType: false,
            success: function (data) {
                // Handle the success response (e.g., display a success message)
                // For simplicity, I'll reload the page to show the newly created workspace
                location.reload();
            },
            error: function (xhr, status, error) {
                // Handle the error response (e.g., display an error message)
            }
        });
    });
});
