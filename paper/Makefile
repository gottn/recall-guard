# Build the preprint: make  (needs latexmk); figures: make figures; table bodies: make tables (both need the repo .venv)
.PHONY: all figures tables clean arxiv
all: main.pdf
main.pdf: main.tex refs.bib fig/fig1_signature.pdf fig/fig2_repair.pdf fig/fig3_tradeoff.pdf tab/signature.tex tab/repair.tex tab/recipes.tex tab/collateral.tex tab/ruler.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null && echo built main.pdf
figures:
	../.venv/bin/python fig/make_figures.py
tables:
	../.venv/bin/python fig/make_tables.py
clean:
	latexmk -C >/dev/null; rm -f main.bbl
# the bundle must compile on its own: source, bibliography, figure PDFs and the generated table bodies
arxiv: main.pdf
	rm -rf arxiv && mkdir -p arxiv/fig arxiv/tab && cp main.tex main.bbl arxiv/ && cp fig/*.pdf arxiv/fig/ && cp tab/*.tex arxiv/tab/ && tar czf arxiv-submission.tar.gz -C arxiv . && rm -rf arxiv && ls -la arxiv-submission.tar.gz
	rm -rf /tmp/rg-arxiv-check && mkdir -p /tmp/rg-arxiv-check && tar xzf arxiv-submission.tar.gz -C /tmp/rg-arxiv-check && cd /tmp/rg-arxiv-check && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null && cmp -s main.tex "$(CURDIR)/main.tex" && echo "bundle compiles on its own and matches main.tex"
