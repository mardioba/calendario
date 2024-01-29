# /home/mardio/Projetos/calendario/calendario/views.py
from django.shortcuts import render, redirect, get_object_or_404
import calendar
import datetime
from .models import Compromisso
from .forms import CompromissoForm, SearchForm, EditCompromissoForm
from django.contrib.auth.decorators import login_required


@login_required
def show_cal(request):
    current_year = datetime.datetime.now().year
    months = []
    form = SearchForm(request.GET)
    for month in range(1, 13):
        # COMPROMISSOS = Compromisso.objects.all()
        COMPROMISSOS = Compromisso.objects.filter(user=request.user, concluido=False)
        month_calendar = calendar.monthcalendar(current_year, month)
        month_name = calendar.month_name[month]
        month_name_pt = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro",
        }[month]

        weeks = []
        for week in month_calendar:
            days = []
            for day in week:
                if day == 0:
                    days.append({"day": "", "link": None, "event_id": None})
                else:
                    link = None
                    event_id = None
                    for compromisso in COMPROMISSOS:
                        if (
                            day == compromisso.data.day
                            and month == compromisso.data.month
                        ):
                            link = (
                                compromisso.get_absolute_url()
                            )  # supondo que você tenha um método get_absolute_url() no modelo Compromisso
                            event_id = compromisso.id
                            break
                    days.append({"day": day, "link": link, "event_id": event_id})
            weeks.append(days)
        total = len(COMPROMISSOS)
        months.append({"month": month_name_pt, "weeks": weeks})
    # print("Total:", total)

    context = {
        "months": months,
        "total": total,
        "form": form,  # Adicione o formulário ao contexto
    }

    return render(request, "calendario/cal.html", context)


@login_required
def add_compromisso(request):
    if request.method == "POST":
        form = CompromissoForm(request.POST)
        if form.is_valid():
            compromisso = form.save(commit=False)
            compromisso.user = request.user  # Define o usuário logado
            compromisso.save()
            return redirect("show_cal")
    else:
        form = CompromissoForm()

    return render(request, "calendario/add_compromisso.html", {"form": form})


@login_required
def compromisso_detail(request, pk):
    compromisso = get_object_or_404(Compromisso, pk=pk)

    # Obtém a data do compromisso
    data_do_compromisso = compromisso.data

    # Filtra todos os compromissos do mesmo dia
    compromissos_do_dia = Compromisso.objects.filter(data=data_do_compromisso)

    return render(
        request, "calendario/compromisso_detail.html", {"compromisso": compromisso, "compromissos_do_dia": compromissos_do_dia}
    )


@login_required
def compromisso_edit(request, pk):
    compromisso = get_object_or_404(Compromisso, pk=pk)

    if request.method == "POST":
        form = EditCompromissoForm(request.POST, instance=compromisso)
        if form.is_valid():
            form.save()
            return redirect("compromisso_detail", pk=pk)
    else:
        form = EditCompromissoForm(instance=compromisso)

    return render(
        request,
        "calendario/compromisso_edit.html",
        {"form": form, "compromisso": compromisso},
    )


@login_required
def compromisso_delete(request, pk):
    compromisso = get_object_or_404(Compromisso, pk=pk)

    if request.method == "POST":
        compromisso.delete()
        return redirect("show_cal")  # ou outra view após a exclusão

    return render(
        request, "calendario/compromisso_delete.html", {"compromisso": compromisso}
    )


@login_required
def search_compromissos(request):
    query = request.GET.get("q")
    compromissos = (
        Compromisso.objects.filter(titulo__icontains=query) if query else None
    )

    return render(
        request,
        "calendario/search_result.html",
        {"compromissos": compromissos, "query": query},
    )
#### CONCLUIR #####
def marcar_concluido(request, compromisso_id):
    compromisso = get_object_or_404(Compromisso, pk=compromisso_id)

    # Marcar o compromisso como concluído
    compromisso.concluido = True
    compromisso.save()

    # Redirecionar para a página de detalhes do compromisso
    return redirect('compromisso_detail', pk=compromisso_id)