
from app.database.conexao import SessionLocal
from app.models.inscricao import Inscricao


class InscricaoRepository:

    def salvar(self, inscricao: Inscricao) -> Inscricao:
        with SessionLocal() as db:
            try:
                if inscricao.id is None:
                    db.add(inscricao)
                else:
                    inscricao = db.merge(inscricao)

                db.commit()
                db.refresh(inscricao)

                return inscricao

            except Exception:
                db.rollback()
                raise

    def buscar_por_id(self, inscricao_id: int) -> Inscricao | None:
        with SessionLocal() as db:
            return db.get(Inscricao, inscricao_id)

    def listar_todos(self) -> list[Inscricao]:
        with SessionLocal() as db:
            return db.query(Inscricao).all()

    def excluir(self, inscricao_id: int) -> bool:
        with SessionLocal() as db:
            inscricao = db.get(Inscricao, inscricao_id)

            if inscricao is None:
                return False

            db.delete(inscricao)
            db.commit()

            return True
