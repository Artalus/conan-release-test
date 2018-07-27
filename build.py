#!/usr/bin/env python3
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(\
        username="Artalus",
        channel='copato-dock',
        remotes="https://api.bintray.com/conan/bincrafters/public-conan",
        build_policy='missing',

        upload="https://api.bintray.com/conan/artalus/conan-public",
        upload_only_recipe=True,
        login_username="Artalus",
    )

    builder.add_common_builds()
    builder.conan_pip_package = 'conan==1.5.0.dev1'
    builder.run()
