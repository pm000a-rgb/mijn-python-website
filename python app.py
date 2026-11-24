<!DOCTYPE html>
<html><head><title>Planning</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="bg-light">
<nav class="navbar navbar-dark bg-dark mb-4"><div class="container d-flex justify-content-between">
<span class="navbar-brand">BouwPlatform</span>
<div>
<a href="{{url_for('dashboard')}}" class="btn btn-outline-light btn-sm me-2">Dashboard</a>
<a href="{{url_for('offertes_lijst')}}" class="btn btn-outline-light btn-sm me-2">Offertes</a>
<a href="{{url_for('klanten')}}" class="btn btn-outline-light btn-sm me-2">Klanten</a>
<a href="{{url_for('projecten_lijst')}}" class="btn btn-outline-light btn-sm me-2">Projecten</a>
<a href="{{url_for('planning')}}" class="btn btn-primary btn-sm me-2">Planning</a>
<a href="{{url_for('logout')}}" class="btn btn-outline-warning btn-sm">Logout</a>
</div></div></nav>
<div class="container">
<h2>Planning</h2>
<div class="card mb-3"><div class="card-body">
<form method="POST" action="{{url_for('planning_nieuw')}}" class="row g-2">
<div class="col-md-3"><input class="form-control" name="naam" placeholder="Wat?" required></div>
<div class="col-md-2"><input class="form-control" name="start_datum" type="date" required></div>
<div class="col-md-2"><input class="form-control" name="eind_datum" type="date" required></div>
<div class="col-md-2"><input class="form-control" name="locatie" placeholder="Locatie"></div>
<div class="col-md-2">
<select name="kleur" class="form-select">
<option value="primary">Blauw</option>
<option value="success">Groen</option>
<option value="warning">Geel</option>
<option value="danger">Rood</option>
</select></div>
<div class="col-12"><button class="btn btn-primary btn-sm">+ Toevoegen</button></div>
</form></div></div>
<h5>Overzicht</h5>
<table class="table table-striped"><tr><th>Wat</th><th>Start</th><th>Eind</th><th>Locatie</th><th>Kleur</th><th></th></tr>
{% for i in items %}
<tr><td>{{i.naam}}</td>
<td>{{i.start_datum.strftime('%d-%m-%Y') if i.start_datum else '-'}}</td>
<td>{{i.eind_datum.strftime('%d-%m-%Y') if i.eind_datum else '-'}}</td>
<td>{{i.locatie or '-'}}</td>
<td><span class="badge bg-{{i.kleur}}">●</span></td>
<td><a href="{{url_for('planning_verwijder',id=i.id)}}" class="btn btn-sm btn-outline-danger">✕</a></td></tr>
{% else %}<tr><td colspan="6">Nog geen planning.</td></tr>{% endfor %}
</table>
</div></body></html>   