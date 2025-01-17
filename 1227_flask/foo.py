<!doctype html>
<html>
    <body>
        <table>
        {% for entry in data %}
            <tr>
                <td>{{ entry[0] }}</td>
	<td>{{ entry[1] }}</td>
	<td>{{ entry[2] }}</td>
            </tr>
        {% endfor %}
        </table>
    </body>
</html>