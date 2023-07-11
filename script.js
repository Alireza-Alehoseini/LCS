$(document).ready(function() {
    $('#compareBtn').click(function() {
        var bodyDna = $('#bodyDna').val();
        var parentsDna = $('#parentsDna').val();

        var data = {
            body_dna: bodyDna,
            parents_dna: parentsDna
        };

        $.ajax({
            url: 'compare_dna',
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json',
            success: function(response) {
                $('#results').html(response);
            }
        });
    });
});
