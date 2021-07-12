from dependency_injector import containers
from dependency_injector import containers, providers
from services.timer_service import TimerService
from services.relay_service import RelayService

class Container(containers.DeclarativeContainer):
  config = providers.Configuration()

  timer_service = providers.Factory(
    TimerService,
  )

  relay_service = providers.Factory(
    RelayService,
  )
    