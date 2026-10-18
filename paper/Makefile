# Build the preprint: make  (needs latexmk); figures: make figures (needs the repo .venv)
all: main.pdf
main.pdf: main.tex refs.bib fig/fig1_signature.pdf fig/fig2_repair.pdf fig/fig3_tradeoff.pdf
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null && echo built main.pdf
figures:
	../.venv/bin/python fig/make_figures.py
clean:
	latexmk -C >/dev/null; rm -f main.bbl
arxiv: main.pdf
	rm -rf arxiv && mkdir -p arxiv/fig && cp main.tex main.bbl arxiv/ && cp fig/*.pdf arxiv/fig/ && tar czf arxiv-submission.tar.gz -C arxiv . && rm -rf arxiv && ls -la arxiv-submission.tar.gz
