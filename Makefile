run:
	@uvicorn games_api.main:app --reload

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(description)	

insert-games:
	@PYTHONPATH=$PYTHONPATH:$(pwd) python -c "import asyncio; from games_api.utils.log_parser import GameProcess; asyncio.run(GameProcess().create_games())"

test:
	@pytest

test-matching:
	@pytest -s -rx -k $(Q) --pdb games_api ./tests/

coverage:
	@pytest --cov=apps --cov=games_api --cov-report=term-missing --cov-report=xml ./tests/	