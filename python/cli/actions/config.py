from cli.config import config
from cli.constants import CLI_DEFAULT_CONFIG_KEY_PASSWORD


def config_func(args):
    if args.set is not None:
        k, v = args.set.split('=')
        config.set(k, v)
        config.save()
        return

    if args.unset is not None:
        k = args.unset
        config.unset(k)
        config.save()
        return

    for k, v in config.data.items():
        if k == CLI_DEFAULT_CONFIG_KEY_PASSWORD:
            continue

        print(f'{k}: {v}')
