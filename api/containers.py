from dependency_injector import containers
from dependency_injector import containers, providers
from services import relay, timer

class Container(containers.DeclarativeContainer):
  config = providers.Configuration()

  timer_service = providers.Factory(
    timer.TimerService,
  )

  relay_service = providers.Factory(
    relay.RelayService,
  )
    