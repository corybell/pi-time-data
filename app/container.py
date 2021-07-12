from dependency_injector import containers
from dependency_injector import containers, providers
from services import relay, option

class AppContainer(containers.DeclarativeContainer):
  config = providers.Configuration()
  config.host.from_env('API_HOST')
  config.port.from_env('API_PORT')
  config.relay_data_file.from_env('RELAY_DATA_FILE')
  config.minute_data_file.from_env('MINUTE_DATA_FILE')
  config.hour_data_file.from_env('HOUR_DATA_FILE')
  config.option_data_file.from_env('OPTION_DATA_FILE')

  option_service = providers.Factory(
    option.OptionService,
    option_file=config.option_data_file
  )

  relay_service = providers.Factory(
    relay.RelayService,
    relay_file=config.relay_data_file
  )
    