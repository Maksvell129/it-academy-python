from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, selectinload
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, insert


class Base(DeclarativeBase):
    pass


class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    checks: Mapped[list["Checks"]] = relationship(
        back_populates="worker"
    )


class Checks(Base):
    __tablename__ = "checks"

    id: Mapped[int] = mapped_column(primary_key=True)

    worker_id: Mapped[int] = mapped_column(
        ForeignKey("workers.id")
    )

    worker: Mapped["Worker"] = relationship(
        back_populates="checks"
    )


engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)


# with Session(engine) as session:
#     worker = Worker(
#         name="Alex"
#     )
#     session.add(worker)
#     session.commit()

with Session(engine) as session:
    statement = select(Worker).where(Worker.name == "Alex")

    worker = session.scalar(statement)

    for order in worker.checks:
        print(order.id)
    else:
        print("У юзера нету чеков")

    session.add(worker)
    session.commit()

# with Session(engine) as session:
#     statement = (
#         select(Worker)
#         .options(selectinload(Worker.checks))
#     )
#
#     workers = session.scalars(statement).all()
#
#     for worker in workers:
#         print(f"Чеки работника: {worker.name}")
#
#         if not  worker.checks:
#             print("У юзера нету чеков")
#         else:
#             for check in worker.checks:
#                 print(check.id)
#
#
#     session.add(worker)
#     session.commit()


# with Session(engine) as session:
#     check = session.get(Checks, 2)
#
#     print(check.id)
#     print(check.worker.name)


# with Session(engine) as session:
#     statement = select(Worker)
#
#     workers = session.scalars(statement).all()
#
#     # print(workers.id, workers.name, workers.email)
#
#     for user in workers:
#         print(user.id, user.name, user.email)

# with Session(engine) as session:
#     statement = select(Worker).where(
#         Worker.email == "maria@example.com"
#     )
#
#     user = session.scalar(statement)
#
# print(user.name, user.email)

