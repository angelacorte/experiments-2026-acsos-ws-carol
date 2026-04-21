## [2.8.0](https://github.com/angelacorte/carol-experiments/compare/2.7.0...2.8.0) (2026-04-20)

### Features

* add node solver property and fix the simulation solver cache ([#72](https://github.com/angelacorte/carol-experiments/issues/72)) ([12f2389](https://github.com/angelacorte/carol-experiments/commit/12f2389e2e4017c19f1ca66a075a598d40b4e27b))

### Dependency updates

* **deps:** update alpine docker tag to v3.23.4 ([2746bfd](https://github.com/angelacorte/carol-experiments/commit/2746bfd7bc1df1eb3ef883d932828d06fbbc3525))
* **deps:** update plugin com.gradle.develocity to v4.4.1 ([77494e7](https://github.com/angelacorte/carol-experiments/commit/77494e7681134e63a36b1ded252052bbd6a89126))

### Build and continuous integration

* **deps:** update actions/setup-node action to v6.4.0 ([bdd8a9f](https://github.com/angelacorte/carol-experiments/commit/bdd8a9f69fc73c7f206f5dc336b109ca1f84642d))

### General maintenance

* **release:** update gradle.properties .env versions to 2.7.0 [skip ci] ([7e3716a](https://github.com/angelacorte/carol-experiments/commit/7e3716a45d37e183e40507c453540633a46b68a1))

## [2.7.0](https://github.com/angelacorte/carol-experiments/compare/2.6.1...2.7.0) (2026-04-20)

### Features

* add simulation run on CI with GRB_LICENSE_FILE ([#53](https://github.com/angelacorte/carol-experiments/issues/53)) ([426d05b](https://github.com/angelacorte/carol-experiments/commit/426d05be8c7694b205731a1e1a04bd83e9b3d58a))

### Dependency updates

* **deps:** update alchemist to v43.0.34 ([b0b2662](https://github.com/angelacorte/carol-experiments/commit/b0b266295d1e77d19ba1b1c88a02321c9ae022bb))
* **deps:** update alchemist to v43.0.35 ([dab39c9](https://github.com/angelacorte/carol-experiments/commit/dab39c9a1dc6df6823e60dfc4e1c84d348dde5bf))
* **deps:** update alchemist to v43.0.37 ([71c2358](https://github.com/angelacorte/carol-experiments/commit/71c2358cccb73ff22691d0c9bdbd071e3d22af76))
* **deps:** update alchemist to v43.0.38 ([391f0c7](https://github.com/angelacorte/carol-experiments/commit/391f0c7d6f19d57fd6034f4d6b351b26d04cabaa))
* **deps:** update dependency xarray to v2026.4.0 ([1dc2719](https://github.com/angelacorte/carol-experiments/commit/1dc2719f89e0e1f1ee4dc3abc9e815f92b628918))
* **deps:** update node.js to 24.15 ([32cc5b5](https://github.com/angelacorte/carol-experiments/commit/32cc5b55c01a46855b39e89377d3c9ae34d4bd25))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.32 ([00264c7](https://github.com/angelacorte/carol-experiments/commit/00264c7133835e78246d344733255e54a05ca5fe))

### General maintenance

* **release:** update gradle.properties .env versions to 2.6.1 [skip ci] ([5f9ba55](https://github.com/angelacorte/carol-experiments/commit/5f9ba551016455ac6447935d95cda8027797777d))

## [2.6.1](https://github.com/angelacorte/carol-experiments/compare/2.6.0...2.6.1) (2026-04-13)

### Bug Fixes

* remove docker and charts from release config ([3a209f1](https://github.com/angelacorte/carol-experiments/commit/3a209f13f006782256eb9543436174a236b72c02))
* temporary change docker gradlew command ([342315e](https://github.com/angelacorte/carol-experiments/commit/342315e7ac072bf8acf025abc05297b034adb532))

### General maintenance

* add license ([35b8328](https://github.com/angelacorte/carol-experiments/commit/35b8328c713dfab4d938a044f2feadd220021364))
* **release:** update gradle.properties .env versions to 2.6.0 [skip ci] ([b77f398](https://github.com/angelacorte/carol-experiments/commit/b77f3980ac8b2cec0c5b900f02514e61232083d9))
* update readme ([a38255e](https://github.com/angelacorte/carol-experiments/commit/a38255eb48762dda4f1517483d0d42b1ea3694f0))

### Style improvements

* adapt to ktlint ([39d05d0](https://github.com/angelacorte/carol-experiments/commit/39d05d09871bb62eef0ebc6cf3325b54433cd3b7))

## [2.6.0](https://github.com/angelacorte/carol-experiments/compare/2.5.0...2.6.0) (2026-04-13)

### Features

* implement follow leader experiment ([#69](https://github.com/angelacorte/carol-experiments/issues/69)) ([c7ded51](https://github.com/angelacorte/carol-experiments/commit/c7ded51bb1f8186f47dbd4eb8c0f813ee8b2df95))

### Dependency updates

* **core-deps:** update collektive to v28.2.3 ([953fe16](https://github.com/angelacorte/carol-experiments/commit/953fe163f55fad92027a0ecc1723a98f58f89e74))
* **deps:** update alchemist to v43.0.32 ([95d2d66](https://github.com/angelacorte/carol-experiments/commit/95d2d66cd08e93ff7a7641f48bdcc214ae27e9ad))
* **deps:** update alchemist to v43.0.33 ([5111a17](https://github.com/angelacorte/carol-experiments/commit/5111a17922519caf1a6d8b5ac01a5142e560bc72))
* **deps:** update python docker tag to v3.14.4 ([b121dad](https://github.com/angelacorte/carol-experiments/commit/b121dada326b738dcd605fc1e1d6785d6f81a3ff))

### Bug Fixes

* remove useless parameter ([#75](https://github.com/angelacorte/carol-experiments/issues/75)) ([58bb21b](https://github.com/angelacorte/carol-experiments/commit/58bb21b904c96593136b5e9e83b3343aa952dd65))
* update minimum distance calculation in CollisionAvoidanceCBF ([#68](https://github.com/angelacorte/carol-experiments/issues/68)) ([9acaae5](https://github.com/angelacorte/carol-experiments/commit/9acaae57bd4b1905cb2a1df764b81a8e3fa6b527))

### General maintenance

* **release:** update gradle.properties .env versions to 2.5.0 [skip ci] ([81be38f](https://github.com/angelacorte/carol-experiments/commit/81be38f0f4960aad9ebc41b2ce7b1a2b0cbef961))

### Refactoring

* rename experiment files ([#74](https://github.com/angelacorte/carol-experiments/issues/74)) ([8fd3b9f](https://github.com/angelacorte/carol-experiments/commit/8fd3b9f9e8b69dee62d437e812896eaddf58c59e))

## [2.5.0](https://github.com/angelacorte/carol-experiments/compare/2.4.3...2.5.0) (2026-04-08)

### Features

* admm with check on owners and initialise models and solver once ([#50](https://github.com/angelacorte/carol-experiments/issues/50)) ([3d5fafd](https://github.com/angelacorte/carol-experiments/commit/3d5fafdc6d7e33b82488c084760b7389f2aa6e6e))

### Dependency updates

* **deps:** update alchemist to v43.0.28 ([3c1f1aa](https://github.com/angelacorte/carol-experiments/commit/3c1f1aa52bbad59ffa9bcd082934373ed190506b))
* **deps:** update alchemist to v43.0.29 ([17d3968](https://github.com/angelacorte/carol-experiments/commit/17d3968ce778f2488b109f4479b4960dfdf2c206))
* **deps:** update alchemist to v43.0.30 ([cd943cb](https://github.com/angelacorte/carol-experiments/commit/cd943cb8dc6da75464f0c697ae22c68545c155a2))
* **deps:** update alchemist to v43.0.31 ([45aedd3](https://github.com/angelacorte/carol-experiments/commit/45aedd3f07e6610cbec00e76c42e957c20ba8984))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.31 ([bb7decf](https://github.com/angelacorte/carol-experiments/commit/bb7decf2be24730e70eef915310fc2db661cc11a))

### General maintenance

* **release:** update gradle.properties .env versions to 2.4.3 [skip ci] ([0fb6565](https://github.com/angelacorte/carol-experiments/commit/0fb6565d72a85e1b5a39dec9fa89200d5c0a5f43))

## [2.4.3](https://github.com/angelacorte/carol-experiments/compare/2.4.2...2.4.3) (2026-04-02)

### Dependency updates

* **core-deps:** update collektive to v28.2.2 ([9195770](https://github.com/angelacorte/carol-experiments/commit/919577020188fa2a241ab5e557253572ad4b9ad4))
* **deps:** update alchemist to v43.0.23 ([431b82c](https://github.com/angelacorte/carol-experiments/commit/431b82c3747e6c1f65d6deb2a5fff5d944a4fda1))
* **deps:** update alchemist to v43.0.24 ([f8f6ec7](https://github.com/angelacorte/carol-experiments/commit/f8f6ec71876277d91e0183c73e67ae0dbd94f85c))
* **deps:** update alchemist to v43.0.25 ([660297d](https://github.com/angelacorte/carol-experiments/commit/660297d1184f53a53b56386186c3c183bc92b300))
* **deps:** update alchemist to v43.0.26 ([54b5781](https://github.com/angelacorte/carol-experiments/commit/54b5781f27685841ba4bb96df6a00ccd8df05165))
* **deps:** update alchemist to v43.0.27 ([faf6c2c](https://github.com/angelacorte/carol-experiments/commit/faf6c2cc09b0b571a0647de1a07b5052d49d4638))
* **deps:** update plugin gitsemver to v7.0.16 ([b20a447](https://github.com/angelacorte/carol-experiments/commit/b20a4471d8c77ec48542da210ac2827a61bea5eb))
* **deps:** update plugin kotlin-qa to v1.3.2 ([57d48d2](https://github.com/angelacorte/carol-experiments/commit/57d48d2f90d78bac86d9d78e655adca1e327ddd9))
* **deps:** update plugin kotlin-qa to v1.4.0 ([ac9938c](https://github.com/angelacorte/carol-experiments/commit/ac9938cef8ce7857e31e545e5f6d8e5af19f3d9d))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.29 ([a7be002](https://github.com/angelacorte/carol-experiments/commit/a7be00245144bc9d15d622337e94e0ea280074ae))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.30 ([76cda0b](https://github.com/angelacorte/carol-experiments/commit/76cda0bf250dc2fa17ab0db6b2e035471ee719bc))

### General maintenance

* **release:** update gradle.properties .env versions to 2.4.2 [skip ci] ([fc2b7b5](https://github.com/angelacorte/carol-experiments/commit/fc2b7b5a97a9ee0b033c90125998d74677a9408f))

## [2.4.2](https://github.com/angelacorte/carol-experiments/compare/2.4.1...2.4.2) (2026-03-25)

### Dependency updates

* **core-deps:** update collektive to v28.2.1 ([bb47fa1](https://github.com/angelacorte/carol-experiments/commit/bb47fa1d107a7599910faf2111de49f8d84699cf))
* **deps:** update alchemist to v43.0.22 ([d46d633](https://github.com/angelacorte/carol-experiments/commit/d46d633b715eeb81d39281b0a7076ec4ded00c81))
* **deps:** update plugin com.gradle.develocity to v4.4.0 ([1efcf30](https://github.com/angelacorte/carol-experiments/commit/1efcf302b85e3e429b5a04f5b05ed87448ee02d3))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.27 ([79fd4b2](https://github.com/angelacorte/carol-experiments/commit/79fd4b2f2e2db086d26c6bc53a41ed0c1ff17c58))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.28 ([5b0578f](https://github.com/angelacorte/carol-experiments/commit/5b0578fa9c2b215560d6956fe232f9e01a7e8beb))

### General maintenance

* **release:** update gradle.properties .env versions to 2.4.1 [skip ci] ([c67afc6](https://github.com/angelacorte/carol-experiments/commit/c67afc6de930a0ea9bb3e1e33d37f575b88c213b))

## [2.4.1](https://github.com/angelacorte/carol-experiments/compare/2.4.0...2.4.1) (2026-03-21)

### Dependency updates

* **core-deps:** update collektive to v28.2.0 ([7c1893b](https://github.com/angelacorte/carol-experiments/commit/7c1893b3d8fc12d79c6491cad7db88ea6ef956e0))
* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.3.20 ([7683861](https://github.com/angelacorte/carol-experiments/commit/7683861f639d200ce504865de5c7e13e48c36bca))
* **deps:** update alchemist to v43.0.20 ([58c84af](https://github.com/angelacorte/carol-experiments/commit/58c84af4409bdfee66f90cbb1e17fb719e87601f))
* **deps:** update gradle to v9.4.1 ([d4ceefa](https://github.com/angelacorte/carol-experiments/commit/d4ceefa95b2e4f106086ee1583be21e75770d501))
* **deps:** update plugin gitsemver to v7.0.15 ([d5e716d](https://github.com/angelacorte/carol-experiments/commit/d5e716d985ee984d8523de64aceb8f091a1baa92))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.25 ([cdd77ee](https://github.com/angelacorte/carol-experiments/commit/cdd77eee1f0ddd884ff0554ff182f5242f46a1c5))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.26 ([#39](https://github.com/angelacorte/carol-experiments/issues/39)) ([5cda0bd](https://github.com/angelacorte/carol-experiments/commit/5cda0bddcd6ac6154f855228b81dd186117bf502))

### General maintenance

* **release:** update gradle.properties .env versions to 2.4.0 [skip ci] ([fb12b71](https://github.com/angelacorte/carol-experiments/commit/fb12b71365b58458ad35ad359bfc214bacea2a9f))

## [2.4.0](https://github.com/angelacorte/carol-experiments/compare/2.3.1...2.4.0) (2026-03-18)

### Features

* add movement strategies for speed and target selection from node molecules ([#36](https://github.com/angelacorte/carol-experiments/issues/36)) ([7a8d125](https://github.com/angelacorte/carol-experiments/commit/7a8d1253aeccbd6ad72d82f837407ba4e292d158))

### Dependency updates

* **deps:** update alchemist to v43.0.19 ([8fa9504](https://github.com/angelacorte/carol-experiments/commit/8fa95042000b2f446453564ba7b63b7ba5eefb67))

### General maintenance

* **release:** update gradle.properties .env versions to 2.3.1 [skip ci] ([34eaf98](https://github.com/angelacorte/carol-experiments/commit/34eaf98f65429de2e8acfcbe3e92b911c094bd81))

## [2.3.1](https://github.com/angelacorte/carol-experiments/compare/2.3.0...2.3.1) (2026-03-18)

### Bug Fixes

* add missing movement action ([#35](https://github.com/angelacorte/carol-experiments/issues/35)) ([d4adad9](https://github.com/angelacorte/carol-experiments/commit/d4adad94f5f6f505eaf43ec86e698b72c22ae68d))

### General maintenance

* **release:** update gradle.properties .env versions to 2.3.0 [skip ci] ([f6a52b5](https://github.com/angelacorte/carol-experiments/commit/f6a52b509206cb66808501a4c3451c93c6e462c5))

## [2.3.0](https://github.com/angelacorte/carol-experiments/compare/2.2.0...2.3.0) (2026-03-17)

### Features

* add more scenarios ([#33](https://github.com/angelacorte/carol-experiments/issues/33)) ([21d7fdc](https://github.com/angelacorte/carol-experiments/commit/21d7fdcb2e3305c9d02296fafa43fb0a2e026f76))

### General maintenance

* **release:** update gradle.properties .env versions to 2.2.0 [skip ci] ([46e69d0](https://github.com/angelacorte/carol-experiments/commit/46e69d0d6bba2fd5dbbb80324fd8d89b7405d382))

## [2.2.0](https://github.com/angelacorte/carol-experiments/compare/2.1.0...2.2.0) (2026-03-17)

### Features

* implement movement model for nodes ([#34](https://github.com/angelacorte/carol-experiments/issues/34)) ([1d796dd](https://github.com/angelacorte/carol-experiments/commit/1d796dd7d8181a21710cc4d3b624643ff80068c9))

### General maintenance

* **release:** update gradle.properties .env versions to 2.1.0 [skip ci] ([f342174](https://github.com/angelacorte/carol-experiments/commit/f342174d761e1425eafebb282e109d03793dc208))

## [2.1.0](https://github.com/angelacorte/carol-experiments/compare/2.0.2...2.1.0) (2026-03-13)

### Features

* add scenario and entrypoint for multiple targets ([#30](https://github.com/angelacorte/carol-experiments/issues/30)) ([2f61739](https://github.com/angelacorte/carol-experiments/commit/2f61739c521a79f7cf60ff3c26bfa7a398708b06))

### General maintenance

* **release:** update gradle.properties .env versions to 2.0.2 [skip ci] ([7a1236a](https://github.com/angelacorte/carol-experiments/commit/7a1236a02e112f80268c62e9cf879eb0b5585430))

## [2.0.2](https://github.com/angelacorte/carol-experiments/compare/2.0.1...2.0.2) (2026-03-13)

### Bug Fixes

* use latest local qp control also for neighboring controls ([#29](https://github.com/angelacorte/carol-experiments/issues/29)) ([5ee4d04](https://github.com/angelacorte/carol-experiments/commit/5ee4d04576bb96d29061cfa1f105c57982769f48))

### General maintenance

* **release:** update gradle.properties .env versions to 2.0.1 [skip ci] ([a34a953](https://github.com/angelacorte/carol-experiments/commit/a34a953c2442400839dd12e6d9747cf7ddf03ccd))

## [2.0.1](https://github.com/angelacorte/carol-experiments/compare/2.0.0...2.0.1) (2026-03-13)

### Bug Fixes

* **ci:** deployment token ([2847199](https://github.com/angelacorte/carol-experiments/commit/28471992abf08fafe8100c36590d1b3e56c870d0))
* **ci:** update workflow logic and permissions for build, deploy, and dispatcher jobs ([#31](https://github.com/angelacorte/carol-experiments/issues/31)) ([a6815bf](https://github.com/angelacorte/carol-experiments/commit/a6815bf5492816c000adbdb686de586ed338d05d))

### General maintenance

* **release:** update gradle.properties .env versions to 2.0.0 [skip ci] ([c105cf1](https://github.com/angelacorte/carol-experiments/commit/c105cf10c4d15276f9d70616d1653f346e6011df))

## [2.0.0](https://github.com/angelacorte/carol-experiments/compare/1.1.2...2.0.0) (2026-03-13)

### ⚠ BREAKING CHANGES

* support CLF/CBF modularity

### Features

* add zero order hold implementation for CBFs and CLFs ([#28](https://github.com/angelacorte/carol-experiments/issues/28)) ([3be8b2b](https://github.com/angelacorte/carol-experiments/commit/3be8b2b6a54407052175457ccfcce8329d3090a6))

### Dependency updates

* **deps:** update alchemist to v42.4.2 ([#17](https://github.com/angelacorte/carol-experiments/issues/17)) ([a4e5808](https://github.com/angelacorte/carol-experiments/commit/a4e5808a27c1babadf5efc03287f03a543246e83))
* **deps:** update alchemist to v43 ([6838f27](https://github.com/angelacorte/carol-experiments/commit/6838f2783c1bd5e70b92edc00d537e4987eeb831))
* **deps:** update dependency xarray to v2026 ([5978bc9](https://github.com/angelacorte/carol-experiments/commit/5978bc90f0fd513994079c57da0ba575a3820fb3))
* **deps:** update node.js to 24.14 ([#20](https://github.com/angelacorte/carol-experiments/issues/20)) ([98f1b02](https://github.com/angelacorte/carol-experiments/commit/98f1b02fcd0eb13f100e1d81f9ba9aad654fcd0d))
* **deps:** update plugin kotlin-qa to v0.101.1 ([#12](https://github.com/angelacorte/carol-experiments/issues/12)) ([774916f](https://github.com/angelacorte/carol-experiments/commit/774916fa2799b5755d452c1d586cdc3289fadd0a))
* **deps:** update plugin kotlin-qa to v1 ([4cae1d7](https://github.com/angelacorte/carol-experiments/commit/4cae1d7e7c27f035d7c437955d8a6de9c132c9ac))

### Bug Fixes

* **ci:** update dispatcher workflow ([8bf1d1f](https://github.com/angelacorte/carol-experiments/commit/8bf1d1f60c4e195d9e9095a165f28fd6c2d13186))
* **ci:** update dispatcher workflow filters and permissions ([f0ca6fd](https://github.com/angelacorte/carol-experiments/commit/f0ca6fd2936b247a826634e3f5afe2e363f24681))
* entrypoint reference ([6c6f921](https://github.com/angelacorte/carol-experiments/commit/6c6f921f45bff060edcfd30f5ffeb52caf304d32))

### Build and continuous integration

* **deps:** update actions/setup-node action to v6.3.0 ([1313383](https://github.com/angelacorte/carol-experiments/commit/1313383b4b38b5b76671da980a5d7f2d71331ee8))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.2 [skip ci] ([5c819f6](https://github.com/angelacorte/carol-experiments/commit/5c819f6f4107062202470817218ba29902f9e740))
* remove old project structure ([b70d8df](https://github.com/angelacorte/carol-experiments/commit/b70d8df92bc4b66c973c3f7ea6259a785f115d1a))
* update readme ([3153145](https://github.com/angelacorte/carol-experiments/commit/315314512e34df2175dd6c13a67badae4b041919))
* update readme ([225e436](https://github.com/angelacorte/carol-experiments/commit/225e436582484dbd843479e17e01b330cbc3e20f))

### Style improvements

* adapt to kotlin qa ([210478a](https://github.com/angelacorte/carol-experiments/commit/210478a37335c7b520ff2c9398016c0291b78cb0))

## [1.1.2](https://github.com/angelacorte/simple-ac-qp-program/compare/1.1.1...1.1.2) (2026-03-11)

### Dependency updates

* **core-deps:** update collektive to v28.1.0 ([#23](https://github.com/angelacorte/simple-ac-qp-program/issues/23)) ([6eec1d3](https://github.com/angelacorte/simple-ac-qp-program/commit/6eec1d35c0f2f3d8d65cf651e00a1ec2f26fdff0))
* **deps:** update gradle to v9.4.0 ([#7](https://github.com/angelacorte/simple-ac-qp-program/issues/7)) ([66c4e6e](https://github.com/angelacorte/simple-ac-qp-program/commit/66c4e6e22b5b02b374b50464208e5568137982f5))

### Build and continuous integration

* **deps:** update actions/checkout action to v6.0.2 ([#11](https://github.com/angelacorte/simple-ac-qp-program/issues/11)) ([dbe9d01](https://github.com/angelacorte/simple-ac-qp-program/commit/dbe9d017c8557c4bdc23156c76cb7c4e4a2e7ec8))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.24 ([#6](https://github.com/angelacorte/simple-ac-qp-program/issues/6)) ([484044d](https://github.com/angelacorte/simple-ac-qp-program/commit/484044d78daf4d65cd7f1d20a148031408b4270a))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.1 [skip ci] ([d8fe8ea](https://github.com/angelacorte/simple-ac-qp-program/commit/d8fe8ea627ce2f693874c22a4b4fbb67ae4be7b0))

## [1.1.1](https://github.com/angelacorte/simple-ac-qp-program/compare/1.1.0...1.1.1) (2026-03-10)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.3.10 ([#1](https://github.com/angelacorte/simple-ac-qp-program/issues/1)) ([d04e521](https://github.com/angelacorte/simple-ac-qp-program/commit/d04e521998f8a7b84b47eeac5a2d05fcfab355e8))
* **deps:** update python docker tag to v3.14.3 ([#15](https://github.com/angelacorte/simple-ac-qp-program/issues/15)) ([1774a7a](https://github.com/angelacorte/simple-ac-qp-program/commit/1774a7a033e8c20b307e835181d559a792fbd48a))

### General maintenance

* **release:** 1.1.1 [skip ci] ([c97fe88](https://github.com/angelacorte/simple-ac-qp-program/commit/c97fe885090d3b56a36a112cd0fc65a02043be02)), closes [#1](https://github.com/angelacorte/simple-ac-qp-program/issues/1)
* **release:** update gradle.properties .env versions to 1.1.0 [skip ci] ([6ff8175](https://github.com/angelacorte/simple-ac-qp-program/commit/6ff817545534ab3c03fb1e441ad50bd73ca69938))

## [1.1.1](https://github.com/angelacorte/simple-ac-qp-program/compare/1.1.0...1.1.1) (2026-03-10)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.3.10 ([#1](https://github.com/angelacorte/simple-ac-qp-program/issues/1)) ([d04e521](https://github.com/angelacorte/simple-ac-qp-program/commit/d04e521998f8a7b84b47eeac5a2d05fcfab355e8))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.0 [skip ci] ([6ff8175](https://github.com/angelacorte/simple-ac-qp-program/commit/6ff817545534ab3c03fb1e441ad50bd73ca69938))

## [1.1.0](https://github.com/angelacorte/simple-ac-qp-program/compare/1.0.0...1.1.0) (2026-03-10)

### Features

* improve reusability and add slack variable into communication range CBF ([#25](https://github.com/angelacorte/simple-ac-qp-program/issues/25)) ([316cb24](https://github.com/angelacorte/simple-ac-qp-program/commit/316cb241e361c2a67a24269c433d1bad2c4b0c25))

### Dependency updates

* **deps:** update alchemist to v42.3.35 ([#8](https://github.com/angelacorte/simple-ac-qp-program/issues/8)) ([1b99299](https://github.com/angelacorte/simple-ac-qp-program/commit/1b9929925510a0d7ef7190ab115befe89a382b4e))
* **deps:** update alpine docker tag to v3.23.3 ([#13](https://github.com/angelacorte/simple-ac-qp-program/issues/13)) ([0b0a79a](https://github.com/angelacorte/simple-ac-qp-program/commit/0b0a79a275ebf0b35216382855f2c4cb30ebde1a))
* **deps:** update dependency com.gurobi:gurobi to v13.0.1 ([#9](https://github.com/angelacorte/simple-ac-qp-program/issues/9)) ([45016d6](https://github.com/angelacorte/simple-ac-qp-program/commit/45016d6704d1320331477bd199a243477fa5b250))
* **deps:** update plugin com.gradle.develocity to v4.3.2 ([#3](https://github.com/angelacorte/simple-ac-qp-program/issues/3)) ([eae92eb](https://github.com/angelacorte/simple-ac-qp-program/commit/eae92ebd0ace09a80a50733d69c1ec6017ed59aa))
* **deps:** update plugin gitsemver to v7.0.13 ([#4](https://github.com/angelacorte/simple-ac-qp-program/issues/4)) ([82b8310](https://github.com/angelacorte/simple-ac-qp-program/commit/82b83105a99a98c6404b4aeab5757716e649dca7))
* **deps:** update plugin kotlin-qa to v0.100.3 ([#5](https://github.com/angelacorte/simple-ac-qp-program/issues/5)) ([65dc9ef](https://github.com/angelacorte/simple-ac-qp-program/commit/65dc9ef940b781a46fffa5ea3fb9183ba69a7c55))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.0 [skip ci] ([b6f6ecd](https://github.com/angelacorte/simple-ac-qp-program/commit/b6f6ecd0f94511014287883b84c801e42b443db1))

## 1.0.0 (2026-03-10)

### Features

* add addRhoNorm2Sq method and removing unused operations ([4a8cce7](https://github.com/angelacorte/simple-ac-qp-program/commit/4a8cce776443a3633de6bc246f8b0fe109ccd39c))
* add ADMM entrypoint with owner mode and configuration files ([9ffb2a3](https://github.com/angelacorte/simple-ac-qp-program/commit/9ffb2a3f33fd10c4654412883df7b516f731095c))
* add Common with utility functions for node movement and license management ([dd538bf](https://github.com/angelacorte/simple-ac-qp-program/commit/dd538bfed1eb0246edff17857e763f319e3bcaef))
* add control barrier functions for obstacle avoidance, communication range, and robot avoidance ([d694916](https://github.com/angelacorte/simple-ac-qp-program/commit/d6949166627550316201acb15adb6e026dab5eca))
* add core ADMM impl ([59d7197](https://github.com/angelacorte/simple-ac-qp-program/commit/59d71974a09e7c047fe2a7de05691dd20073d366))
* add debugging logger ([6654c12](https://github.com/angelacorte/simple-ac-qp-program/commit/6654c122bf4781da7184dae751336337c668c9c0))
* add GRBCommon.kt with optimization utilities and constraints for control systems ([b984086](https://github.com/angelacorte/simple-ac-qp-program/commit/b984086d9aadf1142528d8b16a52ef9505bc6580))
* add location sensor ([834b9fe](https://github.com/angelacorte/simple-ac-qp-program/commit/834b9fe12c47933ae524e9b1ce8d1cf5e18a4f1d))
* add move target in sim setup ([65db350](https://github.com/angelacorte/simple-ac-qp-program/commit/65db350e080b454b662425de5ace37cef456d414))
* add MoveNode class for 2D movement dynamics in the simulation environment ([bba6bad](https://github.com/angelacorte/simple-ac-qp-program/commit/bba6badcc5f21e46526532687303721748eef5a1))
* add MoveTarget class for node movement in Euclidean 2D environment ([7482a4f](https://github.com/angelacorte/simple-ac-qp-program/commit/7482a4fb7f487e4b606a61a0213c864bcc3294bb))
* add operators for SpeedControl2D and average calculation ([3164fb0](https://github.com/angelacorte/simple-ac-qp-program/commit/3164fb008e67f152df1e13cdd08e9cc8537c1dc0))
* add overloaded moveNodeToPosition function to support node ID ([3aecb20](https://github.com/angelacorte/simple-ac-qp-program/commit/3aecb2077aab5ba1057d8991495f9955773de5d0))
* add parameters and control evolution for first part of full ADMM ([d02d838](https://github.com/angelacorte/simple-ac-qp-program/commit/d02d83808aaafefecc237cd385671acf8e7d9727))
* add properties in robot and target data class ([bb40816](https://github.com/angelacorte/simple-ac-qp-program/commit/bb408164dd36e1c2e9001e0be044317bbbb2d1f3))
* add qp with obstacle robot avoidance implementation and configuration files ([5785973](https://github.com/angelacorte/simple-ac-qp-program/commit/57859738f29369096615300b1a34d8472b4b15bc))
* add simple QP with obstacle avoidance ([0e2063e](https://github.com/angelacorte/simple-ac-qp-program/commit/0e2063eae9d4fa01c33a31919f2ac9f49ab4a897))
* add simulation with obstacle and robot avoidance, with communication distance CBF ([49d38c0](https://github.com/angelacorte/simple-ac-qp-program/commit/49d38c0b352c06bab36c4162db27e8a80eb7ef24))
* add speed coercion and rename nominal function for vector control ([128dc96](https://github.com/angelacorte/simple-ac-qp-program/commit/128dc96fa570cc595677e15fff1b5e155eb6beee))
* add SpeedControl2D ([417ac33](https://github.com/angelacorte/simple-ac-qp-program/commit/417ac33115f761ffd6521bdf3b0d75b088c5fa51))
* add utility functions for vector operations in DoubleArrayFuns ([f275707](https://github.com/angelacorte/simple-ac-qp-program/commit/f275707f03de9a11ff027c2ca0a0319df8d6b5a7))
* add vector operations and control functions for Vector2D ([e538d76](https://github.com/angelacorte/simple-ac-qp-program/commit/e538d76da877ecfe02ddc6fca6f2a5e205a10dcd))
* add zeroSpeed function to initialize SpeedControl2D with zero values ([6412d5d](https://github.com/angelacorte/simple-ac-qp-program/commit/6412d5d2035d7e89f30a5ef148851266eef9df8c))
* ADMM control logic with owner mode ([5042194](https://github.com/angelacorte/simple-ac-qp-program/commit/5042194d2d0c37148050627c2df6255ae88f1189))
* ADMM control logic with velocity updates and core ADMM execution ([0e2e47c](https://github.com/angelacorte/simple-ac-qp-program/commit/0e2e47ccd50701c6adea96e1260544e10efa2b71))
* create ADMM base "pseudocode" ([6dc88c4](https://github.com/angelacorte/simple-ac-qp-program/commit/6dc88c453e4182a59150ec3472bbc082276a1182))
* create draw obstacle radius and margin ([528d253](https://github.com/angelacorte/simple-ac-qp-program/commit/528d253b0e61f29eeba77a99ca8b25987ec0f253))
* create first integration of QP with aggregate ([166181d](https://github.com/angelacorte/simple-ac-qp-program/commit/166181d41a6ade83985c9fd7f52ca33a2ab1c5fc))
* enhance ADMM parameters and control evolution for coupled edges ([c9fc070](https://github.com/angelacorte/simple-ac-qp-program/commit/c9fc070c7da63bf3e33b27be2948138c471a68b8))
* enhance GRBModel with logger setup and streamline environment initialization ([78f66f2](https://github.com/angelacorte/simple-ac-qp-program/commit/78f66f24bd05f10166aa01993b441af65325ebf6))
* enhance obstacle rendering with communication area visualization ([6523720](https://github.com/angelacorte/simple-ac-qp-program/commit/6523720dd600f591d90c0ba46997b1df7c8022c6))
* enhance target and robot retrieval functions with ID parameters ([a1ad518](https://github.com/angelacorte/simple-ac-qp-program/commit/a1ad518b0c2936007fed6dd77d92b679d383ba71))
* generalize robot type in control barrier functions ([737a37f](https://github.com/angelacorte/simple-ac-qp-program/commit/737a37fa4561c0c95c4059b30d5fa38cfc6b7478))
* implement centralized control program for basic robot navigation ([2df68ee](https://github.com/angelacorte/simple-ac-qp-program/commit/2df68ee419185d795381afff8db77142ed51765a))
* implement collision avoidance and communication range constraints in ADMM functions ([004606f](https://github.com/angelacorte/simple-ac-qp-program/commit/004606f12b805a0b5eb1bd5240170ddb0de1eca8))
* implement goToTargetCLF function for target convergence in GRBModel ([ddf1209](https://github.com/angelacorte/simple-ac-qp-program/commit/ddf120977b61371588dae55fdb1965667608634a))
* implement local and common ADMM minimization methods in GRBModel ([3ef7e6e](https://github.com/angelacorte/simple-ac-qp-program/commit/3ef7e6e6c0fe2a70f2cf12aab612bee6348e18a0))
* implement local QP without leveraging on neighbor avg ([90abb78](https://github.com/angelacorte/simple-ac-qp-program/commit/90abb78333985d7b29027397d45af1f7f12cbe12))
* implement MoveNode class for 2D movement dynamics in simulation ([0e15cbd](https://github.com/angelacorte/simple-ac-qp-program/commit/0e15cbd45fcc4e7cb01786b5900c5bd909a6309d))
* override toString methods for Coordinate and SpeedControl2D classes ([9a33025](https://github.com/angelacorte/simple-ac-qp-program/commit/9a330256c6c961712bb025b391878a0ee79a0522))
* override toString methods for DualParams, IncidentDuals, and SuggestedControl classes ([165b6ae](https://github.com/angelacorte/simple-ac-qp-program/commit/165b6aebf165c7ec5ad730af6a791ab94a5cecf7))
* refactor ADMM functions to use obstacle avoidance and simplify coupled edge representation ([03d894e](https://github.com/angelacorte/simple-ac-qp-program/commit/03d894ee04da826061e04549dc993c9dd1e26f1e))
* refactor Gurobi license handling and improve logging directory setup ([acad4d9](https://github.com/angelacorte/simple-ac-qp-program/commit/acad4d90b35bd3afe8c7516fa7ad34f94adf8ff8))
* remove ownership ([bffb345](https://github.com/angelacorte/simple-ac-qp-program/commit/bffb3456117c9acb4977029cf246511cb28268d9))
* rename package to 'temp' and update entry points in configuration files ([736bce1](https://github.com/angelacorte/simple-ac-qp-program/commit/736bce13e7f4f3975d0bdfe67466ba87fa68af64))
* update carolADMM configuration ([67b9667](https://github.com/angelacorte/simple-ac-qp-program/commit/67b966708c57e0f70adca6771cb408f7d9904dc0))
* update function calls to use wrongRobotToTargetWithAvoidanceAndDistance for velocity calculation ([c37fcae](https://github.com/angelacorte/simple-ac-qp-program/commit/c37fcae151f5fff43df506d7beee149e2a563c3f))
* update import statements to use DSL for license handling ([e0adafe](https://github.com/angelacorte/simple-ac-qp-program/commit/e0adafe6135716c00171e4d07c5b6c3c84714801))
* update movement program ([87f12aa](https://github.com/angelacorte/simple-ac-qp-program/commit/87f12aa758bb052a9c83caafa7140b060710b858))
* update simpleQPWithObstacle configuration and refactor target movement logic ([aaea8cb](https://github.com/angelacorte/simple-ac-qp-program/commit/aaea8cb39dc764c6d0af136fb40640f652ac0afc))
* update target retrieval to use ID and refactor target movement function ([80d5c55](https://github.com/angelacorte/simple-ac-qp-program/commit/80d5c55298e5072884fcaff6e16adb20e6c97e0c))
* update targetsPosition method to return Target objects instead of Coordinate ([1ba0693](https://github.com/angelacorte/simple-ac-qp-program/commit/1ba0693195198768554e830ce0b969dc902f1ee4))
* use new common avoidance ([77cb059](https://github.com/angelacorte/simple-ac-qp-program/commit/77cb0598dae547130149ab7b20900daa1d18b842))

### Dependency updates

* **deps:** add gurobi dependency ([a582ac3](https://github.com/angelacorte/simple-ac-qp-program/commit/a582ac3632a2263c092019865bfadb8b93673fa5))
* **deps:** update collektive ([aaf5e1e](https://github.com/angelacorte/simple-ac-qp-program/commit/aaf5e1e7bcea11c7ce75890c749d0646a797cd18))

### Bug Fixes

* add robotSafeMargin and robotMaxSpeed variables for improved robot control ([ab9167b](https://github.com/angelacorte/simple-ac-qp-program/commit/ab9167b474f4e8de3b41f21560af316fa298e0f2))
* adjust gamma value in communication range constraint for improved calculations ([4e4dbe1](https://github.com/angelacorte/simple-ac-qp-program/commit/4e4dbe1f6001871fe4bad19f63b1e04fb123dcfb))
* change communication distance ([b5ee626](https://github.com/angelacorte/simple-ac-qp-program/commit/b5ee62638bcddd243ffe8055f00c0f089f5f55c2))
* change communication distance ([aefbbb0](https://github.com/angelacorte/simple-ac-qp-program/commit/aefbbb069c44ac68ad9edd7c3c0142591d5e8740))
* **ci:** add missing permissions ([11e23d0](https://github.com/angelacorte/simple-ac-qp-program/commit/11e23d0a96a9898fc8af1bae3066e3b140dae202))
* **ci:** add missing permissions in dispatcher ([4f3fbda](https://github.com/angelacorte/simple-ac-qp-program/commit/4f3fbdaf24e055e60664df478ae0cc03ea2a1773))
* **ci:** github token secret name ([28dc69b](https://github.com/angelacorte/simple-ac-qp-program/commit/28dc69b56d01158b3be0081d59bd69aab6a57687))
* **ci:** remove charts download ([2eae3da](https://github.com/angelacorte/simple-ac-qp-program/commit/2eae3dadc6a1912775953acce9df9ec955e2e61b))
* **ci:** remove charts workflow ([8539b86](https://github.com/angelacorte/simple-ac-qp-program/commit/8539b86e20840abb48ff9457e66323ca2cc0d7d4))
* **ci:** remove run sim ([8506e21](https://github.com/angelacorte/simple-ac-qp-program/commit/8506e21e3c34d2137f94f151f61a801ca660ffa7))
* correct coefficients in robot avoidance control barrier function ([a703103](https://github.com/angelacorte/simple-ac-qp-program/commit/a70310304c4eae1d5b3f7afb8a4996dcf4a06e0a))
* math sign error ([6d80185](https://github.com/angelacorte/simple-ac-qp-program/commit/6d80185d5fdcdc359e08db3bda9b77243f29155c))
* objective function ([872b7c0](https://github.com/angelacorte/simple-ac-qp-program/commit/872b7c06c40410bb9a179df754137206d2cd27db))
* obstacle avoidance safe margin ([0a3cdf2](https://github.com/angelacorte/simple-ac-qp-program/commit/0a3cdf2570623bf081debeb537568a9d56e45a8b))
* obstacle drawing effect ([c886d36](https://github.com/angelacorte/simple-ac-qp-program/commit/c886d367b88888e851cd559515ca10bff234ba35))
* robot avoidance CBF ([91e1633](https://github.com/angelacorte/simple-ac-qp-program/commit/91e1633685ed5c12da836c66cf0cf7a033766e92))
* simplify control calculations by using direct control arrays ([9bd91ac](https://github.com/angelacorte/simple-ac-qp-program/commit/9bd91ac4ae49e0806a3b87281dc409ab5a1b8235))
* use neighboring instead of share ([736227d](https://github.com/angelacorte/simple-ac-qp-program/commit/736227d3ac8b53fe3e98222f522531e058e6af19))

### Documentation

* add missing documentation ([4db0f10](https://github.com/angelacorte/simple-ac-qp-program/commit/4db0f1071f559b34e974949991881c965adf1a9a))
* better documentation ([5adf839](https://github.com/angelacorte/simple-ac-qp-program/commit/5adf8397480b32dd29c180ef4e9fc2bdf69bff18))

### General maintenance

* add context parameters ([c3fbe7c](https://github.com/angelacorte/simple-ac-qp-program/commit/c3fbe7cf1142b16960b4affa3c12d9f701c64feb))
* add debugging params ([476a30a](https://github.com/angelacorte/simple-ac-qp-program/commit/476a30a570857ab6196146c8f82df6829fdfe193))
* add effects ([4bb13ac](https://github.com/angelacorte/simple-ac-qp-program/commit/4bb13ac0b8e9347c16b96ae03ee170ab34a12a3f))
* add sim yaml for admm ([99724d3](https://github.com/angelacorte/simple-ac-qp-program/commit/99724d36290ca7547a3e5fc8d0b5d5c38a0eb2b3))
* comment old things, some to fix, some to delete, will do ([ad0c0fc](https://github.com/angelacorte/simple-ac-qp-program/commit/ad0c0fcc8db1b57104877deced49080a2587b94d))
* enable Kotlin QA plugin in build configuration ([76c5632](https://github.com/angelacorte/simple-ac-qp-program/commit/76c56325929c39775ad5457a7b7a073335b05858))
* fix math formula ([7896f47](https://github.com/angelacorte/simple-ac-qp-program/commit/7896f47d4edf617da396c34d36543c91b579b80d))
* fix project name ([a7550e1](https://github.com/angelacorte/simple-ac-qp-program/commit/a7550e17958f879cc72a08db9490a7292f493442))
* remove unused import ([bf57d04](https://github.com/angelacorte/simple-ac-qp-program/commit/bf57d04bd6134a7898038bd3eb1098d40518a9d3))
* update .gitignore to include node_modules ([9cb43bc](https://github.com/angelacorte/simple-ac-qp-program/commit/9cb43bcacbf9e09e9fa32032616fb6a90406da2c))
* update communication and obstacle parameters ([afefa67](https://github.com/angelacorte/simple-ac-qp-program/commit/afefa67caa230f414ff1005fb6e7c647c7c698ed))
* update effects ([781549a](https://github.com/angelacorte/simple-ac-qp-program/commit/781549afceb99bf5ccb972237e2ecbe1c780d289))
* update primal and dual tolerance values and increase move target time ([0e63d81](https://github.com/angelacorte/simple-ac-qp-program/commit/0e63d811fe6659c09bc41a644c4a212f19d6212f))

### Style improvements

* adapt to ktlint ([cb484b4](https://github.com/angelacorte/simple-ac-qp-program/commit/cb484b432beb0e61cd4b4e406226e84c2d446538))
* fix indentation ([022f8a3](https://github.com/angelacorte/simple-ac-qp-program/commit/022f8a35327caa946bcd62dde275ed97030e383a))
* no magic numbers ([fbdda58](https://github.com/angelacorte/simple-ac-qp-program/commit/fbdda58d3988a94733193a0c1b0d1d1852c0345b))

### Refactoring

* add error handling for collision avoidance and communication range constraints ([034a8b5](https://github.com/angelacorte/simple-ac-qp-program/commit/034a8b5627c7c9deffd16a2f167c99b412d2d4c2))
* add position property to Target class and update Vector2D interface ([558d9f9](https://github.com/angelacorte/simple-ac-qp-program/commit/558d9f9179a85c536b3b34f25e3672e07c8e3707))
* change return type of addRhoNorm2Sq to Unit for clarity ([f42eb4b](https://github.com/angelacorte/simple-ac-qp-program/commit/f42eb4b7a6a12686bb4cbcb3242b10ff5eff75cb))
* clean up imports and comments in SimpleQP.kt and update entrypoint in simpleQP.yml ([69ab966](https://github.com/angelacorte/simple-ac-qp-program/commit/69ab9660ba21a3af7b6f4596dcde2cec4833506a))
* ControlBarriers and ControLyapunov for improved CBF handling and organization ([22f3925](https://github.com/angelacorte/simple-ac-qp-program/commit/22f392556019cbca07cd6dce8b0cf0357642a270))
* extract local ADMM model setup into a reusable function ([2659dc7](https://github.com/angelacorte/simple-ac-qp-program/commit/2659dc77aed269f3a12a20d6300865c9a4845bac))
* generalize robot type ([91091a7](https://github.com/angelacorte/simple-ac-qp-program/commit/91091a7f82c2982e28af014c9f7fafa9b08894a2))
* improve rendering logic in DrawObstacleRadius and enhance visibility checks ([8c7751f](https://github.com/angelacorte/simple-ac-qp-program/commit/8c7751f23d4d8647d50f7857c484d6711356550c))
* improve variable naming and add comments for clarity ([354114c](https://github.com/angelacorte/simple-ac-qp-program/commit/354114c16750d58700eb09caa458dbbe34337230))
* move coordinates into proper file ([787bd95](https://github.com/angelacorte/simple-ac-qp-program/commit/787bd950b780783cabec74d7f634fb385d6d05fd))
* move data classes for control and dual parameters into proper file ([58b9a48](https://github.com/angelacorte/simple-ac-qp-program/commit/58b9a481f486e31a69eba553c30dbd8b8194a241))
* move functionalities into proper package and reuse external functions ([9790cc2](https://github.com/angelacorte/simple-ac-qp-program/commit/9790cc2fbbac82ffb246a1a98f03731038584db7))
* move robot movement functions and improve license handling ([3682cf6](https://github.com/angelacorte/simple-ac-qp-program/commit/3682cf62f0185cc4ea2f1061088a8075b022b56a))
* parameterize tolerance and iteration settings in ADMM ([1607019](https://github.com/angelacorte/simple-ac-qp-program/commit/160701991861773af9a333204f11b29a0e4e6387))
* put common function into proper file ([c60acd5](https://github.com/angelacorte/simple-ac-qp-program/commit/c60acd5115e342ff9a0588d79ad9baf9d263e759))
* remove commented-out fullADMM and executeCoreADMM functions ([1ecf8a4](https://github.com/angelacorte/simple-ac-qp-program/commit/1ecf8a4971365b2f4c51bd669988b36de86b4f28))
* remove generic ID type from Robot instances and update control parameter handling ([046bf8f](https://github.com/angelacorte/simple-ac-qp-program/commit/046bf8fec6a9d31f7f84b0e77688f93acf6e7b81))
* remove generic ID type from robot parameters ([7493b6a](https://github.com/angelacorte/simple-ac-qp-program/commit/7493b6ac385d241afd794ea2366eb0f711a52469))
* remove old robot-avoidance and communication-range control barrier functions ([0e267b2](https://github.com/angelacorte/simple-ac-qp-program/commit/0e267b2f01f11935a4d58f3301e4bcb9b838cac7))
* remove unused effects ([5f088fa](https://github.com/angelacorte/simple-ac-qp-program/commit/5f088fa0e3928d7de64016d4c77e9a494cfc6a30))
* remove unused entrypoints ([2326f74](https://github.com/angelacorte/simple-ac-qp-program/commit/2326f7429c3dd6b7c98699b5cac1b34d73d7114f))
* remove unused entrypoints ([9a75211](https://github.com/angelacorte/simple-ac-qp-program/commit/9a752110e28c3638bebdc2ec23689aca8e660bd7))
* remove unused executeBeforeUpdateDistribution function ([846788f](https://github.com/angelacorte/simple-ac-qp-program/commit/846788fa44df8b0816f5edb23015670d08b51249))
* remove unused moveTargetTo ([ea6d1c9](https://github.com/angelacorte/simple-ac-qp-program/commit/ea6d1c9721e4f10312f7ecff48a9e91f4656d42f))
* rename admm function to coreADMM ([b9da92c](https://github.com/angelacorte/simple-ac-qp-program/commit/b9da92ce26a9b17aa297bad449e86224bf4e2da6))
* rename ADMM.kt and update package structure for better organization ([70db885](https://github.com/angelacorte/simple-ac-qp-program/commit/70db8852648d3bd1e6334814c3098bc2b4f45012))
* rename LocalUpdate to IncidentDuals and update related data structures for clarity ([7b307ff](https://github.com/angelacorte/simple-ac-qp-program/commit/7b307ff1acb6c5d4a3f6b8973d0e8d83503beeb9))
* rename Point interface to Point2D and update related data classes ([df18e19](https://github.com/angelacorte/simple-ac-qp-program/commit/df18e19d4d50611ccc5f48915e7fae5efce93109))
* rename Point2D to Vector2D ([1bcd49d](https://github.com/angelacorte/simple-ac-qp-program/commit/1bcd49d420e8aefbf4ae2e72c8a68931150735f5))
* rename variables ([49aaa56](https://github.com/angelacorte/simple-ac-qp-program/commit/49aaa567dba36863f95ff26a206d33c9488bb117))
* reorganize ADMM.kt by adding control loop and residual update functions ([1073b09](https://github.com/angelacorte/simple-ac-qp-program/commit/1073b09d458ce1a8fd22af5b4a4b9e9b601a344a))
* replace ScalarVector with DoubleArray for consistency in control functions ([891074e](https://github.com/angelacorte/simple-ac-qp-program/commit/891074e789370754da5b142a5347d40d23d42161))
* robot control function ([72b33a4](https://github.com/angelacorte/simple-ac-qp-program/commit/72b33a463f461cb5a2edd090859bf2afb8944e26))
* simplify getRobot and getRobotsToAvoid functions by removing unnecessary parameters ([8324683](https://github.com/angelacorte/simple-ac-qp-program/commit/83246830ce4676cabf70c6f27c72db74db2c6b5e))
* simplify LocationSensorProperty by removing unused parameters ([c5c48e2](https://github.com/angelacorte/simple-ac-qp-program/commit/c5c48e2ba2dec7cd4431ab2ed6ee5dcc99bf7108))
* simplify obstacle avoidance and communication range functions by removing generic ID type ([e03c9fb](https://github.com/angelacorte/simple-ac-qp-program/commit/e03c9fb56ca8dc02c66e14393e793464785e6bee))
* simplify Robot class by removing generic ID ([b7e6a51](https://github.com/angelacorte/simple-ac-qp-program/commit/b7e6a5196691f506b2f7f431b618360a109978da))
* specify type for localInfos as Robot<Int> ([b15ad74](https://github.com/angelacorte/simple-ac-qp-program/commit/b15ad74a0081f9915e1ef167794c32edace2b0e7))
* streamline optimization result handling in Minimization.kt ([46bc378](https://github.com/angelacorte/simple-ac-qp-program/commit/46bc37835cae87e8f1c6171d56fa0db01d703917))
* streamline residual update functions and improve control application logic ([ab21225](https://github.com/angelacorte/simple-ac-qp-program/commit/ab2122511a61241afc89257709ea30a21769aa2a))
* typo in filename ([a1627c1](https://github.com/angelacorte/simple-ac-qp-program/commit/a1627c171eb837a8a3c271b929bf65d19ddb0a72))
* update control loop to use dual parameters and remove unused avg calculation ([71469d7](https://github.com/angelacorte/simple-ac-qp-program/commit/71469d7836d0ef80d5150be168a65cd6135c20e6))
* update minimizeADMMCommonQP to use IncidentDuals and improve error handling ([f9f8f76](https://github.com/angelacorte/simple-ac-qp-program/commit/f9f8f7697621913056ca97cd4b3884fdd6f5632d))
* update minimizeADMMLocalQP and minimizeADMMCommonQP to remove generic ID type and improve parameter handling ([239b0ab](https://github.com/angelacorte/simple-ac-qp-program/commit/239b0ab9c4ea0e15982104ce04ada47f6c0032db))
* update moveNodeToPosition function to use Point2D type ([a774d73](https://github.com/angelacorte/simple-ac-qp-program/commit/a774d7386914350b86ebc63df0378f5d32ba422d))
* update package structure and remove unused imports in Functionalities.kt ([4304eb8](https://github.com/angelacorte/simple-ac-qp-program/commit/4304eb824c5f06e7891c9cc58a135e1ffe5be590))
* update residualUpdate functions to return Residuals type ([4368e86](https://github.com/angelacorte/simple-ac-qp-program/commit/4368e863daa8ce5afd67779b863875a8d8b79ad1))
* update robotAvoidanceAndCommunicationRangeCBF to use optional range parameter and incidentDuals ([201db25](https://github.com/angelacorte/simple-ac-qp-program/commit/201db2519c3a4b344ce96a8e9b456fd07fa4880e))
* update robotToTargetWithAvoidanceAndDistance function calls to include neighboring robots ([7e84e1d](https://github.com/angelacorte/simple-ac-qp-program/commit/7e84e1d21cd266be0350298f8fac659e91c78c5f))
* update variable names and comments in SimpleQP.kt for clarity ([822ff65](https://github.com/angelacorte/simple-ac-qp-program/commit/822ff6593caa6b017b0a5229e582a1ae3a5616c1))

## [1.1.21](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.20...1.1.21) (2025-11-25)

### Bug Fixes

* **gradient example:** specifying incarnation as first parameter ([#485](https://github.com/Collektive/collektive-experiments-bootstrap/issues/485)) ([ae4b426](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ae4b426ed43ec11651b9743410a97cfece8976d7))

### Build and continuous integration

* **deps:** update actions/setup-python action to v6.1.0 ([#484](https://github.com/Collektive/collektive-experiments-bootstrap/issues/484)) ([994aee1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/994aee1278215ae308ffa2134c06f6fce8d6ea3b))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.20 [skip ci] ([c0e0970](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c0e0970e8b956706eae02938c85bc1810ecc469f))

## [1.1.20](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.19...1.1.20) (2025-11-21)

### Dependency updates

* **core-deps:** update collektive to v27.4.0 (minor) ([#483](https://github.com/Collektive/collektive-experiments-bootstrap/issues/483)) ([cfdf7cc](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cfdf7ccb712203893a955da3729addfa49a48020))
* **deps:** update alchemist to v42.3.17 (patch) ([#469](https://github.com/Collektive/collektive-experiments-bootstrap/issues/469)) ([62194fb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/62194fb4bfd1eb229afc712ee82d4d4ae9d3361e))
* **deps:** update alchemist to v42.3.18 (patch) ([#474](https://github.com/Collektive/collektive-experiments-bootstrap/issues/474)) ([c8e2113](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c8e2113d0b4d4e1a8883cdf1d4cbd545ac886580))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.155 ([#470](https://github.com/Collektive/collektive-experiments-bootstrap/issues/470)) ([be631c8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/be631c864a5026fe348a9ad15be8cf361b1c3473))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.156 ([#472](https://github.com/Collektive/collektive-experiments-bootstrap/issues/472)) ([97d84a5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/97d84a5ee5f2987ec731dcc20d17698fbda579f9))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.157 ([#482](https://github.com/Collektive/collektive-experiments-bootstrap/issues/482)) ([7feb7e3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7feb7e331bce70fe9475abc42796a57fe0b4f886))
* **deps:** update dependency xarray to v2025.11.0 ([#480](https://github.com/Collektive/collektive-experiments-bootstrap/issues/480)) ([0f75d5d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0f75d5d469778970408fad04bab4069f8d7cc332))
* **deps:** update gradle to v9.2.1 ([#475](https://github.com/Collektive/collektive-experiments-bootstrap/issues/475)) ([cd52e67](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cd52e6741d563082f18c1be31370b1f160b17092))
* **deps:** update plugin gitsemver to v7.0.7 ([#479](https://github.com/Collektive/collektive-experiments-bootstrap/issues/479)) ([1ed14f5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1ed14f557b2533e69264bfdbb756cc5126942f49))
* **deps:** update plugin kotlin-qa to v0.97.0 ([#471](https://github.com/Collektive/collektive-experiments-bootstrap/issues/471)) ([f8655aa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f8655aa0cd5151ae4ddfb1406b43265b2c5b7f43))
* **deps:** update plugin kotlin-qa to v0.98.0 ([#473](https://github.com/Collektive/collektive-experiments-bootstrap/issues/473)) ([ae033a7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ae033a77ee974225352b17c2c41e91a8512e4573))
* **deps:** update plugin kotlin-qa to v0.98.1 ([#476](https://github.com/Collektive/collektive-experiments-bootstrap/issues/476)) ([1821a83](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1821a83e4947df113094579985b42a3c8ecec162))
* **deps:** update plugin kotlin-qa to v0.98.2 ([#478](https://github.com/Collektive/collektive-experiments-bootstrap/issues/478)) ([63a699b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/63a699bfd356fa260183ca7ef418a8893d3e14c9))

### Build and continuous integration

* **deps:** update actions/checkout action to v5.0.1 ([#477](https://github.com/Collektive/collektive-experiments-bootstrap/issues/477)) ([e7c8c31](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e7c8c315d81967dc8deca9ba1fc25126ac181d2c))
* **deps:** update actions/checkout action to v6 ([#481](https://github.com/Collektive/collektive-experiments-bootstrap/issues/481)) ([d63594c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d63594c99be5799688a280d4f650f8f7cda7871a))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.19 [skip ci] ([19b9965](https://github.com/Collektive/collektive-experiments-bootstrap/commit/19b9965bf541a7dfc0445ab5ff5a97ecbf855fae))

## [1.1.19](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.18...1.1.19) (2025-11-12)

### Dependency updates

* **core-deps:** update collektive to v27.3.3 (patch) ([#468](https://github.com/Collektive/collektive-experiments-bootstrap/issues/468)) ([76f9970](https://github.com/Collektive/collektive-experiments-bootstrap/commit/76f99703d2caddc1b5ebcbd7972e79972dac35d4))
* **deps:** update alchemist to v42.3.14 (patch) ([#449](https://github.com/Collektive/collektive-experiments-bootstrap/issues/449)) ([ff8b690](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ff8b690d2473ee41702462f5322582045492c1a4))
* **deps:** update alchemist to v42.3.15 (patch) ([#453](https://github.com/Collektive/collektive-experiments-bootstrap/issues/453)) ([cf1dcc0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cf1dcc0384bb556106b933c26cbad7ddb719e30b))
* **deps:** update alchemist to v42.3.16 (patch) ([#466](https://github.com/Collektive/collektive-experiments-bootstrap/issues/466)) ([afa6615](https://github.com/Collektive/collektive-experiments-bootstrap/commit/afa6615b90eab02f09a25dd9b18e62e27a6e1908))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.150 ([#454](https://github.com/Collektive/collektive-experiments-bootstrap/issues/454)) ([80435f2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/80435f27f3491e94d0238756e8f9da2696e1cabc))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.151 ([#455](https://github.com/Collektive/collektive-experiments-bootstrap/issues/455)) ([9e3b04d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9e3b04dcd6ee1b2ad315132bf61f06f5c866f45b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.152 ([#456](https://github.com/Collektive/collektive-experiments-bootstrap/issues/456)) ([d4f0d7b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d4f0d7b9c0b1e21bd15f057e478db8b77348d13e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.153 ([#464](https://github.com/Collektive/collektive-experiments-bootstrap/issues/464)) ([fdefc74](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fdefc7442b6833ea054373845908fbfd83f95b63))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.154 ([#467](https://github.com/Collektive/collektive-experiments-bootstrap/issues/467)) ([bd563e4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bd563e49fb01be8bd95bbe0110b7790d756da6ae))
* **deps:** update gradle to v9.2.0 ([#459](https://github.com/Collektive/collektive-experiments-bootstrap/issues/459)) ([05547b9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/05547b9209a07722b3565ca49898df7d9bea6344))
* **deps:** update node.js to v24 ([#461](https://github.com/Collektive/collektive-experiments-bootstrap/issues/461)) ([8ee3b49](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8ee3b497d2190c6a2c41e4c851555e3b2dc39514))
* **deps:** update plugin gitsemver to v7.0.6 ([#457](https://github.com/Collektive/collektive-experiments-bootstrap/issues/457)) ([7a03e6e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7a03e6ee6bf1c2efa125825899e5f83092f33414))
* **deps:** update plugin kotlin-qa to v0.95.2 ([#448](https://github.com/Collektive/collektive-experiments-bootstrap/issues/448)) ([2f75808](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2f75808bd7e0fc2b991db4b919683c5d1ab1650c))
* **deps:** update plugin kotlin-qa to v0.95.3 ([#460](https://github.com/Collektive/collektive-experiments-bootstrap/issues/460)) ([ec6b569](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ec6b56936fc19ba7a8e8c25f387fde65415a4581))
* **deps:** update plugin kotlin-qa to v0.96.0 ([#462](https://github.com/Collektive/collektive-experiments-bootstrap/issues/462)) ([1c2a417](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c2a41702debcc3e025aaa1757b9a09072d5c9d1))
* **deps:** update plugin multijvmtesting to v4.3.1 ([#450](https://github.com/Collektive/collektive-experiments-bootstrap/issues/450)) ([df54648](https://github.com/Collektive/collektive-experiments-bootstrap/commit/df5464845e62643c914bc70a265ec96e185f4f50))
* **deps:** update plugin multijvmtesting to v4.3.2 ([#458](https://github.com/Collektive/collektive-experiments-bootstrap/issues/458)) ([2082411](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2082411f2d0495ba071c4c6e67c39590dfae5f23))

### Build and continuous integration

* **deps:** update actions/download-artifact action to v6 ([#451](https://github.com/Collektive/collektive-experiments-bootstrap/issues/451)) ([7c14281](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7c14281eaa3b9e852bbc71a6760a7c85f3a5b170))
* **deps:** update actions/upload-artifact action to v5 ([#452](https://github.com/Collektive/collektive-experiments-bootstrap/issues/452)) ([8d4ec31](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8d4ec31a4ba7fa442aa3a1ba12576ef6c4c51640))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.11 ([#463](https://github.com/Collektive/collektive-experiments-bootstrap/issues/463)) ([cd82bbf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cd82bbfa345ca0d24d3504cefc8ae90f3ff8c773))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.12 ([#465](https://github.com/Collektive/collektive-experiments-bootstrap/issues/465)) ([2fb0efb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2fb0efbbc4ba50e221d1deddbe3bed474a03d41a))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.18 [skip ci] ([081e522](https://github.com/Collektive/collektive-experiments-bootstrap/commit/081e522ab263572cb7771eb35340f2f68cb0adef))

## [1.1.18](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.17...1.1.18) (2025-10-23)

### Dependency updates

* **core-deps:** update collektive to v27.3.2 (patch) ([#446](https://github.com/Collektive/collektive-experiments-bootstrap/issues/446)) ([4531ac0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4531ac0d22b4c3ffe2371943f79a29bce19d1d82))
* **deps:** update plugin gitsemver to v7.0.5 ([#447](https://github.com/Collektive/collektive-experiments-bootstrap/issues/447)) ([7b84bf9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7b84bf9019ffd6161f54290192afb7d442090e39))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.17 [skip ci] ([1645fa5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1645fa551908da7fc74007785c3362d99c732cfd))

## [1.1.17](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.16...1.1.17) (2025-10-23)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.2.21 ([#445](https://github.com/Collektive/collektive-experiments-bootstrap/issues/445)) ([3a428da](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3a428daf10b3b92805007cc0a30321a4a17bf9aa))
* **deps:** update node.js to 22.21 ([#444](https://github.com/Collektive/collektive-experiments-bootstrap/issues/444)) ([81b2567](https://github.com/Collektive/collektive-experiments-bootstrap/commit/81b256742e3ff6a3c188d410d1641ed679469eaa))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.16 [skip ci] ([aa08caf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/aa08caf0bfdb79ad88dd6255bb3d0a020abd9093))

## [1.1.16](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.15...1.1.16) (2025-10-22)

### Dependency updates

* **core-deps:** update collektive to v27.2.0 ([f63ae0b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f63ae0bc31b0cdb5a4598ff3373123c8a3a2c2f4))
* **core-deps:** update collektive to v27.3.0 ([5edcbf1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5edcbf1b3b093b12f95f7dda0930f036aae682fd))
* **core-deps:** update collektive to v27.3.1 ([df64107](https://github.com/Collektive/collektive-experiments-bootstrap/commit/df641075e911503839c728cfc70bbb38b42aa17e))
* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.2.20 ([af1dd9b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/af1dd9be0d1ff7662fe1cbbf97fc9115141cf680))
* **deps:** update alchemist to v42.2.10 ([cb922ac](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cb922ac5a38927f50a4cd784b74937a54ea49920))
* **deps:** update alchemist to v42.2.11 ([ccce26c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ccce26c21918b2752bb2b35c1eb7abd4e1e80ae7))
* **deps:** update alchemist to v42.2.13 ([c597c55](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c597c55b39646dcd354ff88ad873d8667fbb22c9))
* **deps:** update alchemist to v42.2.14 ([5c8c65a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5c8c65a731e5156d94a105049f952b69000a45b8))
* **deps:** update alchemist to v42.2.16 ([513071b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/513071bc06b6a723f5241da3ee3df8f230406f27))
* **deps:** update alchemist to v42.2.17 ([33e3a29](https://github.com/Collektive/collektive-experiments-bootstrap/commit/33e3a290324c9c90148675dad3b966793a0d7d4c))
* **deps:** update alchemist to v42.3.0 ([dcc416e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dcc416e018582bc396072f7105d97e66e58f27a8))
* **deps:** update alchemist to v42.3.1 ([7c61ac4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7c61ac413aeeee4b71856d9d67f37e51a7a529a2))
* **deps:** update alchemist to v42.3.10 ([14de05a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/14de05aa56f7fc0893ae9b34e9eb2cef5cc981d2))
* **deps:** update alchemist to v42.3.11 ([f827de0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f827de090f7c25b51809957778cd544349aff3c4))
* **deps:** update alchemist to v42.3.12 ([4d5043f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4d5043f7d1f02d88aefbdbdfbf03428b6e195b54))
* **deps:** update alchemist to v42.3.13 ([941f3eb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/941f3ebd23cfda439c216d886a12e45e90f20a27))
* **deps:** update alchemist to v42.3.2 ([5fb7f03](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5fb7f03c6253427a52fa3a07b3c4352f32530448))
* **deps:** update alchemist to v42.3.3 ([2bba8f9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2bba8f9cc225bebf0f487463c8fd9d4e716341cc))
* **deps:** update alchemist to v42.3.4 ([6cae629](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6cae629d53c1e846524c8739c99a86f2ee2b1904))
* **deps:** update alchemist to v42.3.5 ([21a044e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/21a044e02cf4380d96e72a21ff990882b1604d4c))
* **deps:** update alchemist to v42.3.6 ([b10b77c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b10b77c754149c675b31ddb7876fd78d544456fc))
* **deps:** update alchemist to v42.3.7 ([dbefc76](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dbefc7651a9dcb30b227729e5013da6b84215294))
* **deps:** update alchemist to v42.3.8 ([ed7fc02](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ed7fc02810810d44569327cefb0d9671d5a38094))
* **deps:** update alchemist to v42.3.9 ([1278cc4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1278cc4bf988df6c304f4fdadfc5ff0d4a980f61))
* **deps:** update alpine docker tag to v3.22.2 ([ce7ece2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ce7ece207fe5c0291bfb4bf922ecd321bd261341))
* **deps:** update collektive to v27.1.0 ([e01d96e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e01d96e52e4bc31d4a0a930794cab25c70516f19))
* **deps:** update dependency matplotlib to v3.10.6 ([3c85022](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3c850222c66296c2a9cb1ee3d471209e92bbab29))
* **deps:** update dependency matplotlib to v3.10.7 ([e4fd7d6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e4fd7d6d03e8f47e5292c5984d822febebdb767b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.140 ([3ee92d6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3ee92d63a98de97c6ee66805abc535ec9e6bf702))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.141 ([04debc6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/04debc6d5951680309a1ec5aeb8f0771a01c3518))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.142 ([9a8e12a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9a8e12ac6cb3873590908513b0cff816880633b0))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.143 ([46690d4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/46690d4adb2a48397db17f08cf2b3aa02c76306b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.144 ([b089053](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b08905369adf28e775ff7fc4d0fcec3ef4ca07b3))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.145 ([bd4a212](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bd4a212cf3ebf7a6ee500b72c4e9247320b9f567))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.146 ([f64ce9a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f64ce9a9b25cbe48beab214c228b9d4f5b1a4b42))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.147 ([83b9c92](https://github.com/Collektive/collektive-experiments-bootstrap/commit/83b9c9255e919e13743b61efb4285a89aaddc5e7))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.148 ([347c2c2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/347c2c2425f97494317b28d0bf04e15f64154066))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.149 ([b2ab0ed](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b2ab0ed1d4ce34ad1f0e1ed97845ec8482df338d))
* **deps:** update dependency xarray to v2025.10.0 ([610412d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/610412d2f48ede6a956c96a7802c9c40abd6ff0b))
* **deps:** update dependency xarray to v2025.10.1 ([fa36267](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fa36267ac292fc9198d7640a4f9001d6660e8ea0))
* **deps:** update dependency xarray to v2025.8.0 ([248cc79](https://github.com/Collektive/collektive-experiments-bootstrap/commit/248cc7904317b61045f0d905bbfe1c0a071cb709))
* **deps:** update dependency xarray to v2025.9.0 ([c673e9a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c673e9a051475c677159ce5f7763febcc6a35701))
* **deps:** update dependency xarray to v2025.9.1 ([02eebfa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/02eebfa30893e6719a34ad29c20ead3799955dc3))
* **deps:** update eclipse-temurin docker tag to v25 ([0d9cef8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0d9cef87b9f4f8a194ef52320a06ea39eec089d9))
* **deps:** update gradle to v9.1.0 ([a5f9a54](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a5f9a54d0d10d2613a79a980c74c9801fe3247ba))
* **deps:** update node.js to 22.19 ([27f052f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/27f052f85c5cd5f5f8aa12dda19455332828aa9e))
* **deps:** update node.js to 22.20 ([e12922e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e12922e410cd900bb02730e652e6bbabfb89ec50))
* **deps:** update plugin com.gradle.develocity to v4.1.1 ([6a4898c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6a4898c5f62f11226b773421360901ad7f77af39))
* **deps:** update plugin com.gradle.develocity to v4.2 ([4543de1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4543de1f9e8111bccbe415661f875b1f9201cbbd))
* **deps:** update plugin com.gradle.develocity to v4.2.1 ([6e05ac3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6e05ac37be8ec74ab2da5ca2e214a4c46fe88a28))
* **deps:** update plugin com.gradle.develocity to v4.2.2 ([f593833](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f59383368de2afd670a221ee6dfdb865941884fd))
* **deps:** update plugin gitsemver to v6.0.2 ([335c0ba](https://github.com/Collektive/collektive-experiments-bootstrap/commit/335c0ba1d2d03ce37e3f1c89f00ba01912250319))
* **deps:** update plugin gitsemver to v7 ([64c5360](https://github.com/Collektive/collektive-experiments-bootstrap/commit/64c536053b7148c5eb591593b44c2529f7e59f48))
* **deps:** update plugin gitsemver to v7.0.2 ([99bbd56](https://github.com/Collektive/collektive-experiments-bootstrap/commit/99bbd56ff209aad5c5db1fbc2797b93ea1467201))
* **deps:** update plugin gitsemver to v7.0.3 ([3f77c75](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3f77c75acfa38be7c6983e4819e18f1463b5bcec))
* **deps:** update plugin gitsemver to v7.0.4 ([b652dcf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b652dcf22a19ca62d8b39d191dc9129dbdeedc59))
* **deps:** update plugin kotlin-qa to v0.93.3 ([8b9078d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8b9078df0cff3f9a9a29892a0920f3976b382f4e))
* **deps:** update plugin kotlin-qa to v0.94.0 ([b0fdbca](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b0fdbca7073b81611f1245cf6b8ab0c20114d34e))
* **deps:** update plugin kotlin-qa to v0.95.1 ([f6254a3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f6254a306ec7dafb754e2550cb8545246efb91dd))
* **deps:** update plugin multijvmtesting to v4 ([09781e8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/09781e81876e2fe146d0507e6a09d54e1b58d54a))
* **deps:** update python docker tag to v3.13.7 ([2ea4608](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2ea46083f7acb92ba7609b115b4efc604258c869))
* **deps:** update python docker tag to v3.13.8 ([e2ac11b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e2ac11bd34ef3d36bd488f9d3ae7dbc9b672b500))
* **deps:** update python docker tag to v3.14.0 ([61cab24](https://github.com/Collektive/collektive-experiments-bootstrap/commit/61cab24bf3846a6511374b0c09e98b728abbbd93))

### Bug Fixes

* **build:** correct jvm version ([1884cd5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1884cd5c86c06deb2b9bc04627ee208315162976))
* remove obsolet version attribute ([2f482a4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2f482a45ede094aacfd22a7ffdbdff8c537ec223))

### Build and continuous integration

* **deps:** update actions/setup-node action to v5 ([8ca8941](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8ca8941b9a62de7271295a82edbb2f51b8750690))
* **deps:** update actions/setup-node action to v6 ([a603ec0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a603ec0e1c63cd79946c2ec9f43fe1c213e965b9))
* **deps:** update actions/setup-python action to v6 ([110c2fe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/110c2fedafab2c967b1c44a2880b92cb5c3a5b49))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.10 ([4820e5c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4820e5c3f5808098a09756fee6c6b64f438a14ec))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.4 ([c5afcf9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c5afcf96a3b36391a1354d7bf65a2574521fb763))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.5 ([4405a13](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4405a1349cb4884e9191f1318212d20b9bd9d66a))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.6 ([a2731ba](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a2731ba09109c048d2bc2b174b85f57b29bdeff4))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.7 ([0775a52](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0775a5288a30283541c7dcc01d283c3f8a4b3804))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.8 ([50f7642](https://github.com/Collektive/collektive-experiments-bootstrap/commit/50f7642170026ec5f57eae0ffacdb8afa89c7430))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.9 ([5b8c5f1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5b8c5f1a008745330eb6ce5a75d0ac8666fe0e23))

### General maintenance

* comment charts generation ([8604e72](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8604e726619ceaa8d476dbbad9643d7610fa200f))
* **release:** update gradle.properties .env versions to 1.1.15 [skip ci] ([1cf1388](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1cf1388c8b58abbea9ae27b7dfaa53969d4c59ce))

## [1.1.15](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.14...1.1.15) (2025-08-16)

### Dependency updates

* **core-deps:** update collektive to v26.1.2 ([4085f22](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4085f225a470aa9c4b2c261d378db9bd15b108bc))
* **deps:** update plugin kotlin-qa to v0.93.2 ([93eb586](https://github.com/Collektive/collektive-experiments-bootstrap/commit/93eb58616f9812c7ca0ec5fcfc768f508a2b0987))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.14 [skip ci] ([926211d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/926211dcd3c089b9aafa4578c1d9d117325237d8))

## [1.1.14](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.13...1.1.14) (2025-08-16)

### Dependency updates

* **core-deps:** update collektive to v26 and org.jetbrains.kotlin.jvm to v2.2.10 ([1f1c291](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1f1c291a6260811dc0481b4604de59a0b0b1b2c8))
* **deps:** update alchemist to v42.2.9 ([54a3cd5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/54a3cd5d6ea46792d861768c6e957efd9a85a524))
* **deps:** update dependency gradle to v9 ([08044ad](https://github.com/Collektive/collektive-experiments-bootstrap/commit/08044adb53a5c9c617d6d18511a98c71a5301c28))
* **deps:** update dependency matplotlib to v3.10.5 ([e52d8d7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e52d8d7c8866e2cce07145c62d6ebe6f4e938926))
* **deps:** update node.js to 22.18 ([#351](https://github.com/Collektive/collektive-experiments-bootstrap/issues/351)) ([9ac8c52](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9ac8c521e066ebe525bbd39e0d3ebf95e72548f3))
* **deps:** update plugin gitsemver to v5.1.8 ([a841dc5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a841dc5a8a26b3fad6b568d78b3f26a006dadb6e))
* **deps:** update plugin gitsemver to v6 ([66e3b92](https://github.com/Collektive/collektive-experiments-bootstrap/commit/66e3b92e62b50ae8d9498b0d4ee4807e8967f696))
* **deps:** update plugin gitsemver to v6.0.1 ([c191cb5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c191cb5852c30923462a74d42bdeda91e217bff5))
* **deps:** update plugin kotlin-qa to v0.93.1 ([#334](https://github.com/Collektive/collektive-experiments-bootstrap/issues/334)) ([c17700a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c17700adbbbce2f846e9f69ff5ae03b2eabde6ca))
* **deps:** update plugin multijvmtesting to v4 ([#356](https://github.com/Collektive/collektive-experiments-bootstrap/issues/356)) ([2a1b709](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2a1b709457ba1cad50b32eeaa9440698e4fdd134))
* **deps:** update python docker tag to v3.13.6 ([65ac6a7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/65ac6a7401f458af0e03ca707cd91dd494d623d4))

### Build and continuous integration

* compute the available memory in pure Kotlin ([1936527](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1936527e87e44193b2284946fe54687e1854d555))
* **deps:** update actions/checkout action to v4.3.0 ([7f2bbd4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7f2bbd4268eb70f4360aa6229c2fa03d304514f0))
* **deps:** update actions/checkout action to v5 ([d9cb943](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d9cb9432c5bf08e44f372d689a9edb8cd1848788))
* **deps:** update actions/download-artifact action to v5 ([3717686](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3717686b3d5f9cb373040e672d070f78c96fe62b))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.3 ([38c775e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/38c775ea9fbb0b2f0c8932bd25b26cb1791ab06e))
* migrate to develocity ([5bacf24](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5bacf2461ad8fd708b337f71acd304dce0ae0ae1))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.13 [skip ci] ([4634c2d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4634c2dbefb6b6f093355cc6cb1c2681e91cbe60))

### Style improvements

* import the ktlint rules from Alchemist ([1c39ea9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c39ea9d9452d11dded0cc35b910e3928cbe1d32))

## [1.1.13](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.12...1.1.13) (2025-08-07)

### Dependency updates

* **core-deps:** update collektive to v25.0.2 ([540323f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/540323f74ee0c6ef7a1dde4f77d2353a5a837cf0))
* **deps:** update alchemist to v42.2.2 ([df2ac26](https://github.com/Collektive/collektive-experiments-bootstrap/commit/df2ac26fafcacb7d83ba02c5aeb59ea0a0282ae4))
* **deps:** update alchemist to v42.2.3 ([8148523](https://github.com/Collektive/collektive-experiments-bootstrap/commit/814852331016fa7d4776e14e1ec3dc51749cf0e8))
* **deps:** update alchemist to v42.2.4 ([ffd481e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ffd481ef6e2f4d1d4496cfa3771a97484bb00006))
* **deps:** update alchemist to v42.2.5 ([e9783d7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e9783d79497eda08dded7a2bb33e9d41ce6ea948))
* **deps:** update alchemist to v42.2.6 ([464e239](https://github.com/Collektive/collektive-experiments-bootstrap/commit/464e2392ac2c6d52288df930c79129299189823e))
* **deps:** update alchemist to v42.2.7 ([dbc304a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dbc304a6d0c9b147f9af24b75c1346c4905fec24))
* **deps:** update alchemist to v42.2.8 ([a9f0885](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a9f088536058b2d05456219606ce4fd303606d24))
* **deps:** update alpine docker tag to v3.22.0 ([616987b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/616987b0cae3ef0ed89213152414ba5659be9cac))
* **deps:** update alpine docker tag to v3.22.1 ([5e4e69b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5e4e69b1a6ab33ab70417aa8de2482910a263a6d))
* **deps:** update dependency gradle to v8.14.2 ([dcaf58a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dcaf58ad73ae721a496e7d5e5826528a7b5c4def))
* **deps:** update dependency gradle to v8.14.3 ([6d1c710](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6d1c71064c8744ce1b85a2006966fe8e0254d8b0))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.132 ([87fc84b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/87fc84bba799448fc40043332787ea68af4ad04a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.133 ([9a9ea27](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9a9ea278ca729ef7d365117ea91614d5396ef642))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.135 ([769940e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/769940eaf8b35be68d373d2f0c69c8bcf66196ee))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.136 ([32dddaf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/32dddafbce3cb2cc416dd5a42b7f5bb7a0f3b3e1))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.137 ([1c75410](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c754106986d3aeced329048f9917c306ac2a563))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.138 ([4dee4d7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4dee4d7a0050461a075b5d1f37d311127524570d))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.139 ([f798d2e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f798d2e5fc4d2b6bc0b620b4b76d1f1b6a9c9f52))
* **deps:** update dependency xarray to v2025.6.1 ([0d51cee](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0d51ceef69d43ccdac18422103e16d58a7e99c8c))
* **deps:** update dependency xarray to v2025.7.0 ([6e3f5c2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6e3f5c25bbd08821340e0e901680c785e35c0fdb))
* **deps:** update dependency xarray to v2025.7.1 ([09ed6c1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/09ed6c1ab44beb88a360af64755809a88e6e1465))
* **deps:** update node.js to 22.17 ([d044937](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d044937d97c5651865380e3cc8de701f2cd62116))
* **deps:** update plugin gitsemver to v5.1.4 ([2db6d10](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2db6d10996c0ffb9992d13fe29c1d0a1ac9913ee))
* **deps:** update plugin gitsemver to v5.1.7 ([36a2780](https://github.com/Collektive/collektive-experiments-bootstrap/commit/36a27805f7482c26898fc64fc2406527ccaf31e6))
* **deps:** update plugin kotlin-qa to v0.89.0 ([0347341](https://github.com/Collektive/collektive-experiments-bootstrap/commit/034734108dc8d98abebfd13f1789b91782de8642))
* **deps:** update plugin kotlin-qa to v0.89.1 ([ff913a8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ff913a85ca7dd18447f3b6c5b57558eadcb2be80))
* **deps:** update plugin multijvmtesting to v3.5.0 ([c28bd46](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c28bd4693def06eaad9ad44b486c81455af828f4))
* **deps:** update plugin multijvmtesting to v3.5.1 ([42f53a6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/42f53a6e0a72393469a3a2d06586eb9146bc081a))
* **deps:** update python docker tag to v3.13.4 ([c62d528](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c62d528518834a3749f9fa4b7843988770bf77da))
* **deps:** update python docker tag to v3.13.5 ([9deba83](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9deba834800e6fd31d0cb1fdadabe9f8b72a0ac4))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v4 ([94e1b98](https://github.com/Collektive/collektive-experiments-bootstrap/commit/94e1b98cddd5c3dddb1d877fd19cfd778dd1c518))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.1 ([46cc85c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/46cc85c52d5be4e591db3a7889fcdf121f0d35c8))
* **deps:** update danysk/build-check-deploy-gradle-action action to v4.0.2 ([b36a1cd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b36a1cdf5723d635a1e7739ce0d5d70da4bb0470))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.12 [skip ci] ([82620aa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/82620aa59bbfaedf4c50e27fa37d8eb36f9282e3))

## [1.1.12](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.11...1.1.12) (2025-05-26)

### Dependency updates

* **core-deps:** update collektive to v25.0.1 ([7fc4d0f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7fc4d0faa5cfbfbb1de478fbd289804a611b7c22))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.11 [skip ci] ([c0e857b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c0e857be4ba132969d4b4dfd3cd7957fb85c60ad))

## [1.1.11](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.10...1.1.11) (2025-05-26)

### Dependency updates

* **core-deps:** update collektive to v25 ([d0bfb72](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d0bfb722a86a1121f7a14f022755df55bb30a97c))
* **deps:** update alchemist to v42.2.1 ([1e67ecf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1e67ecfd2775538768a6c703787d09a5c36b450a))
* **deps:** update plugin kotlin-qa to v0.88.0 ([8e9c655](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8e9c655b7c08c0597dc1f18499fcf9ed1dbd016f))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.10 [skip ci] ([846e5c8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/846e5c8b2611a81c8d84aadbb035ab7ea13be2e5))

## [1.1.10](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.9...1.1.10) (2025-05-23)

### Dependency updates

* **core-deps:** update collektive to v24.0.10 ([ae6c79a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ae6c79ac0c8667eec3be24c503b77be845bff17d))
* **deps:** update dependency gradle to v8.14.1 ([7551384](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7551384a145ee0f9f45789218a05fcca051b5dfc))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.129 ([874c7d2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/874c7d25b29f0e36083b037fc62c8d30ab99a535))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.131 ([877fd47](https://github.com/Collektive/collektive-experiments-bootstrap/commit/877fd47c4944448c68e31d4497ce26cd5813d106))
* **deps:** update node.js to 22.16 ([60886ef](https://github.com/Collektive/collektive-experiments-bootstrap/commit/60886ef6241847c8bcf7b238b99d5baa4bddc287))
* **deps:** update plugin kotlin-qa to v0.87.0 ([e1b674d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e1b674d1fd053f506c9d1948f6f54c056e0067fa))
* **deps:** update plugin kotlin-qa to v0.87.1 ([e969f78](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e969f7854dc8a87f4bb10cee37a5bb0b49a3365e))
* **deps:** update plugin multijvmtesting to v3.4.3 ([a3081ae](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a3081ae8ded473af1a6efeb51b238df10500a37e))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.9 [skip ci] ([88185d6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/88185d61cfd95e69597957a60715142491fe504a))

## [1.1.9](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.8...1.1.9) (2025-05-19)

### Dependency updates

* **core-deps:** update collektive to v24.0.9 ([bce9f6f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bce9f6f01fa06a8c49d10780eb0e0b361870536a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.128 ([397f75f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/397f75faadaa05b9f356e9aa1ef04beb86871390))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v1 ([ba51fc6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ba51fc6441c60963c630327aca8679d6175b7600))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.19 ([e8f51b2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e8f51b2dc87fe48004a3968bda2fac1b90927dcb))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.20 ([62e6d70](https://github.com/Collektive/collektive-experiments-bootstrap/commit/62e6d70f41f0be29b5cda4af5c41e56242a366d6))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.8 [skip ci] ([6687470](https://github.com/Collektive/collektive-experiments-bootstrap/commit/668747014b417df321bdf15988edc060e3b62089))

## [1.1.8](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.7...1.1.8) (2025-05-15)

### Dependency updates

* **core-deps:** update collektive to v24.0.8 ([5f5418f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5f5418ffae88bef1ab93da96dafe557b2a7bae73))
* **deps:** update alchemist to v42.1.1 ([25a017f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/25a017fff3f1d582bb0c063784699be88b283d2f))
* **deps:** update alchemist to v42.2.0 ([e8fca01](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e8fca01ff5baf121f85cb9110da10d7db219c84a))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.7 [skip ci] ([d00a7fa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d00a7fa9cde062a2db0a3b33aa101343420a0def))

## [1.1.7](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.6...1.1.7) (2025-05-13)

### Dependency updates

* **core-deps:** update collektive to v24.0.6 ([4701bb5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4701bb554aa85dc5bdc0d8517fda52ba8ed666c8))
* **deps:** update plugin gitsemver to v5.1.3 ([f3dfb61](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f3dfb61dc55025d3f715076bea386be14fd4a58a))
* **deps:** update plugin kotlin-qa to v0.86.2 ([e2d422f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e2d422ffa7d32b72c63c3588bd23046178f8ded1))
* **deps:** update plugin multijvmtesting to v3.4.2 ([a744526](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a74452630b6dd66f6f271c3a7a61e8ba2bd24b19))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.6 [skip ci] ([b9e7f56](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b9e7f5663b93dfdfeca39e88a5666a25b7a72044))

## [1.1.6](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.5...1.1.6) (2025-05-13)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.1.21 ([1c63823](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c63823f9fc3b6a427a071a210b34a439e6793eb))
* **deps:** update dependency matplotlib to v3.10.3 ([930c774](https://github.com/Collektive/collektive-experiments-bootstrap/commit/930c7747b645db31cabf0e232c3b55d19796efd7))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.5 [skip ci] ([a607965](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a607965c1d462d736c5d1c04c26e5bfe1ff50fa9))

## [1.1.5](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.4...1.1.5) (2025-05-05)

### Dependency updates

* **core-deps:** update collektive to v24.0.5 ([d42e396](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d42e39676d61a3fe224099d9de19adc5bc822e19))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.4 [skip ci] ([0f58e9b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0f58e9b945c379750e7599923f53d85ef8c0edc2))
* update readme ([f0f319b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f0f319baedd0d01663aceeec9ce37b92edfe3942))

## [1.1.4](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.3...1.1.4) (2025-05-04)

### Dependency updates

* **core-deps:** update collektive to v24.0.4 ([5f53e24](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5f53e24fcefa51abdce3ad0c69b1f92c2f3aca8b))
* **deps:** update dependency xarray to v2025.4.0 ([86a9389](https://github.com/Collektive/collektive-experiments-bootstrap/commit/86a9389918515bf180119220ae8ea1d11a894081))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.18 ([bc9fe77](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bc9fe776462d3094c3f2361502badb1d27a9bc1b))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.3 [skip ci] ([bfa607d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bfa607d68a16dbc2279f8cc044fffef2ec0c3fe6))

## [1.1.3](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.2...1.1.3) (2025-05-02)

### Dependency updates

* **core-deps:** update collektive to v24.0.3 ([0e3f87a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0e3f87aa5c98e4b342b81d8a22cb5978388ac390))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.2 [skip ci] ([24f4e16](https://github.com/Collektive/collektive-experiments-bootstrap/commit/24f4e16b277c7ea0de382a6a433fcc17ff634628))

## [1.1.2](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.1...1.1.2) (2025-05-01)

### Dependency updates

* **core-deps:** update collektive to v24.0.2 ([9df3296](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9df3296afa4eb01df66183b1f07b40392bd3b7f2))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.1 [skip ci] ([69ff521](https://github.com/Collektive/collektive-experiments-bootstrap/commit/69ff521327d3ca6a2c878068867c87f5f9917869))

## [1.1.1](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.1.0...1.1.1) (2025-05-01)

### Dependency updates

* **core-deps:** update collektive to v24.0.1 ([f2996de](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f2996de7e3543fcaa84d0d694b4fc6dfa7557ad3))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.127 ([72462bc](https://github.com/Collektive/collektive-experiments-bootstrap/commit/72462bc3a20c3636c14d00d2a435d8f045042dd6))

### General maintenance

* **release:** update gradle.properties .env versions to 1.1.0 [skip ci] ([ca10ef1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ca10ef189d0c1abf05672515d6e1b40f7e1b5a92))

## [1.1.0](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.58...1.1.0) (2025-04-30)

### Features

* add hooks and checks in CI ([#275](https://github.com/Collektive/collektive-experiments-bootstrap/issues/275)) ([48fb2a2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/48fb2a25c8505c766d72283708804df0a4007eb2))

### Dependency updates

* **core-deps:** update dependency it.unibo.collektive.collektive-plugin to v24 ([ee5133d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ee5133d324d94a4e879b050ec65b6b17793c3874))

### Bug Fixes

* gradient due to disalignment ([a50271c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a50271c6740d7c5c6891762966b8cf756f58ef5e))
* remove hooks ([366c369](https://github.com/Collektive/collektive-experiments-bootstrap/commit/366c3695855cadb4f18c1b0a397d7c8e0097c578))
* remove java launcher ([7590812](https://github.com/Collektive/collektive-experiments-bootstrap/commit/75908126945d662fe126516e9e43e6dc898a4492))

### Documentation

* rephrase kdoc ([4e97205](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4e9720517cbb7bda805be084f026a55fe03b1d2b))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.58 [skip ci] ([c4a132b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c4a132beb131f2ec33e0b48cc2e63aa052e23660))

### Style improvements

* fix according to ktlint ([213a2e0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/213a2e0948d8993b996290123a3aaf597575f363))

## [1.0.58](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.57...1.0.58) (2025-04-28)

### Dependency updates

* **core-deps:** update collektive to v23 ([0418c1b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0418c1b8cf256351be9e594d045073948769203f))
* **deps:** update alchemist to v42.0.9 ([add5527](https://github.com/Collektive/collektive-experiments-bootstrap/commit/add5527033194fc1fb1edf5b78ee13acb4915a5e))
* **deps:** update alchemist to v42.1.0 ([3f6b96b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3f6b96bf7631f8b2a458801eb6f59aa6ff1fc35a))
* **deps:** update dependency gradle to v8.14 ([8595101](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8595101ba54c085a6c1a9a8579d232489bfae236))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.126 ([92271e8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/92271e8e860118da5cfb1461acac96d94a7f5803))
* **deps:** update node.js to 22.15 ([49c6693](https://github.com/Collektive/collektive-experiments-bootstrap/commit/49c669305cee5e92a130187172d03cdfce11d501))
* **deps:** update plugin gitsemver to v5.1.2 ([53f0791](https://github.com/Collektive/collektive-experiments-bootstrap/commit/53f0791c1ea91886a6a8e3789edeee3463b9fe56))
* **deps:** update plugin kotlin-qa to v0.86.1 ([ee9a0fe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ee9a0fe3f03399a6feaf031b46d749aa5ad6828f))
* **deps:** update plugin multijvmtesting to v3.4.1 ([4b8efc1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4b8efc1f3488395b6f2ac162960072bafa09c6d6))

### Bug Fixes

* adapt to collektive v23.0.4 ([821f4fe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/821f4fe33dde90f83cb2b6c65b7bd41d03bb9559))
* **deps:** remove useless plugin use in bundles ([d411fa7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d411fa74d05e459629ef2a6f17058ef4c2f6ea16))

### Build and continuous integration

* **deps:** update actions/download-artifact action to v4.3.0 ([ea06e6e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ea06e6e9894b7652e0b252b28527ed3713f761bd))
* **deps:** update actions/setup-python action to v5.6.0 ([e0fc345](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e0fc345c7262f930b53383bfb65ae40f29f27cfc))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.57 [skip ci] ([1a9b793](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1a9b7933d2bfe4903b8477df47367d742a5c7960))

## [1.0.57](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.56...1.0.57) (2025-04-19)

### Dependency updates

* **core-deps:** update collektive to v22.3.2 ([3acd140](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3acd140c36eb6ccf68fe8f9980a41e59e229b8bb))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.56 [skip ci] ([a725af7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a725af7be812c6712c5858477e6d45be481c0080))

## [1.0.56](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.55...1.0.56) (2025-04-16)

### Dependency updates

* **core-deps:** update collektive to v22.3.1 ([78c68cb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/78c68cb86d2779988814cd28811e02a5270ccb34))
* **deps:** update plugin multijvmtesting to v3.4.0 ([3f69b58](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3f69b585567bdceb84fd81e006bce9c16edfb71a))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.55 [skip ci] ([62b09a4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/62b09a42759d3c00c8a19190b087bde13b31ece4))

## [1.0.55](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.54...1.0.55) (2025-04-16)

### Dependency updates

* **core-deps:** update collektive to v22.3.0 ([1ca7867](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1ca78675ab47bc1973b81af9e21e5f47eb18d3fa))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.54 [skip ci] ([5f86cbd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5f86cbd3c1b909d3a5028d0df1b8c4e6ca7eb1de))

## [1.0.54](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.53...1.0.54) (2025-04-16)

### Dependency updates

* **core-deps:** update collektive to v22.2.0 ([c2fcc10](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c2fcc10385cac74617ef0de82a0cdd228dffed5b))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.53 [skip ci] ([8ce03a9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8ce03a9824f8f11b793764eb26303df3ff6dbd83))

## [1.0.53](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.52...1.0.53) (2025-04-14)

### Dependency updates

* **core-deps:** update collektive to v22.0.1 ([bce996d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bce996d83bc15b1383d9bf5e6a94a32e58f2a0e6))
* **deps:** update alchemist to v42.0.8 ([1b61572](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1b6157280dd8c67e576623c553235d0e9c14862b))
* **deps:** update plugin gitsemver to v5 ([138f76d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/138f76d1b3523ed50c8f242bc06b90906ed90b1d))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.17 ([8e379c4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8e379c4cedc5a998ffc16de50389005b8cdd2b10))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.52 [skip ci] ([104e553](https://github.com/Collektive/collektive-experiments-bootstrap/commit/104e5536032f2ac2d0991470c334d63f1b84b420))

## [1.0.52](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.51...1.0.52) (2025-04-14)

### Dependency updates

* **core-deps:** update collektive to v22 ([27e54cb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/27e54cbcae0d7c9135b9712f065ba02dae3a00e5))
* **deps:** adapt to collektive v22 ([63d853c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/63d853ce4dc6987b848631b1cfe4b0246df9032c))
* **deps:** update python docker tag to v3.13.3 ([81a839d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/81a839d37743a9653f5dbbc051b1833fa72b0616))

### Bug Fixes

* collektive version ([97d40b3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/97d40b375ecd0ee2a9abe8bfc23b38086c0e9336))
* typo ([b6f0e97](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b6f0e97a412e261328ba9d7c824e9a8f00ee9020))

### Build and continuous integration

* **deps:** update actions/setup-node action to v4.4.0 ([13a6da3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/13a6da3d8ccb5dd88e7813ef845ddbc7a00d44f6))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.51 [skip ci] ([a8cf4a9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a8cf4a9f3ab4e827bcb5e841d20016268840213d))

## [1.0.51](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.50...1.0.51) (2025-04-11)

### Dependency updates

* **core-deps:** update collektive to v21 ([6b98662](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6b98662a99ba80e773a8897a4dafbed968d700d1))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.50 [skip ci] ([ba6be7f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ba6be7f988d9f4c22b85c2132a794572294a4747))

## [1.0.50](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.49...1.0.50) (2025-04-10)

### Dependency updates

* **core-deps:** update collektive to v20.2.3 ([dd981a6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dd981a6dae4ff47f3d2f85d8c570c3cdd7d3cec6))
* **deps:** update alchemist to v42.0.7 ([b88735a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b88735a12a8c910d18a156ac47b30940edd9b668))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.10.0 ([b2d64cd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b2d64cdb3b5625bde370d419eda7147c217f40d9))

### Bug Fixes

* adapt to collektive v20.2.3 patch ([2aa82e2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2aa82e26e829ff5055a171eae1cfd6edec704833))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.16 ([b853a41](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b853a41b3198c868b5233b1bc6570880fb7f1e96))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.49 [skip ci] ([10c7cdf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/10c7cdfb748e2b408f202937c3ed9fa053026728))

## [1.0.49](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.48...1.0.49) (2025-04-09)

### Dependency updates

* **core-deps:** update collektive to v20.2.2 ([73b1200](https://github.com/Collektive/collektive-experiments-bootstrap/commit/73b1200ce95b40c2d19345e5ce784a85a25b5042))
* **deps:** update alchemist to v42.0.6 ([bf73ed0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bf73ed0ce1b9577cf19f40bb452d5b54449d5c1f))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.15 ([e06e919](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e06e919a88fb8a48eb78c334abfb8246b697b107))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.48 [skip ci] ([3cbca0c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3cbca0c3531394a1b630a92039a3b99faa4a65b8))

## [1.0.48](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.47...1.0.48) (2025-04-08)

### Dependency updates

* **core-deps:** update collektive to v20.2.1 ([1a6fd6a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1a6fd6a55fb2c8ce5ae8dda02bcea7d249f4a50e))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.47 [skip ci] ([0a90374](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0a903747998531b7263c8a0ac89e2415124d5dfc))

## [1.0.47](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.46...1.0.47) (2025-04-08)

### Dependency updates

* **core-deps:** update collektive to v19.1.0 ([ad3da05](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ad3da059104c7f2180a1dcfad5a8a75b2916649f))
* **core-deps:** update collektive to v20 ([5c9f815](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5c9f815c7e0996cadf8567e5d559b1251531f313))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.46 [skip ci] ([5d99e28](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5d99e2834cb4f40a423f8e81300e716bbb75e0c8))

## [1.0.46](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.45...1.0.46) (2025-04-07)

### Dependency updates

* **core-deps:** update collektive to v19 ([ee48a60](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ee48a608dd493c7285b5ffc2e0a7e1342ab65b51))
* **deps:** update dependency xarray to v2025.3.1 ([625b682](https://github.com/Collektive/collektive-experiments-bootstrap/commit/625b6824ecfe0569f5b861a8f9bffdaf75314340))

### Bug Fixes

* adapt to Collektive v19 ([7801f3e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7801f3e0e4eeda9e9870b2e9409f1c818055d953))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.45 [skip ci] ([30df006](https://github.com/Collektive/collektive-experiments-bootstrap/commit/30df0063a2a437fb3993ffc7e03c561c27e3d858))

## [1.0.45](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.44...1.0.45) (2025-04-02)

### Dependency updates

* **core-deps:** update collektive to v17.2.2 ([96675e1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/96675e17c920199b5bf0b72e5d2e9c9adafe7fc4))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.44 [skip ci] ([639d1f5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/639d1f5c1110b4d11233a1be4ec824d2e51d17d3))

## [1.0.44](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.43...1.0.44) (2025-04-01)

### Dependency updates

* **core-deps:** update collektive to v17.2.1 ([2541c18](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2541c18304ccfac944ac45fea358e01eacb9266e))
* **deps:** update alchemist to v42.0.2 ([53a057d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/53a057df612efa10d2a08db96a3a698cda178af9))
* **deps:** update alchemist to v42.0.3 ([5d93da3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5d93da3121e8442c797aa04c09cdafc1eea3795e))
* **deps:** update alchemist to v42.0.4 ([9a41792](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9a417928faa9e654048eaf1b264915eb66de5c53))
* **deps:** update alchemist to v42.0.5 ([cc3d8c5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cc3d8c5c71b72c2e9ce8830c69ae54ca102105db))
* **deps:** update plugin kotlin-qa to v0.84.1 ([7eecbae](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7eecbaebe924a62796a30574341ffe3131315bc8))
* **deps:** update plugin kotlin-qa to v0.85.0 ([f8edf0b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f8edf0b589858054a4e7d53f165e1b3db0b040f6))

### Build and continuous integration

* **deps:** update actions/setup-python action to v5.5.0 ([9be0823](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9be0823d659a64c2618bfaf34460154462fc030a))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.14 ([72f20a0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/72f20a05b9b40615f31d07c2a9e74af576f369ab))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.43 [skip ci] ([562da44](https://github.com/Collektive/collektive-experiments-bootstrap/commit/562da44ce0cc23dd1ce219843d25eda1ec1785a8))

## [1.0.43](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.42...1.0.43) (2025-03-24)

### Dependency updates

* **core-deps:** update collektive to v17.2.0 ([fb6410b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fb6410be5fbf5fa5371b788b2d2c85fa60117d24))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.42 [skip ci] ([51d06c8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/51d06c8579826727f897154ebc3af0bd9aeb6323))

## [1.0.42](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.41...1.0.42) (2025-03-23)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.1.20 ([1f47d60](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1f47d60f2049dd662f38541c18670d6ac3a199a3))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.41 [skip ci] ([f8dfa0a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f8dfa0a6e42032236a16cb6f64a20c5f1ac39aa3))

## [1.0.41](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.40...1.0.41) (2025-03-23)

### Dependency updates

* **core-deps:** update collektive to v17.1.3 ([3f859f6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3f859f63f7904c1f3d9441e660317f243c6727a4))
* **deps:** update dependency xarray to v2025.3.0 ([f72c93b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f72c93b7a62cc56d5504e2718cf165eeb831bab2))
* **deps:** update plugin multijvmtesting to v3.3.0 ([0cea2c3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0cea2c357b9e03af9ed831f5c0f9329f43a9e1a4))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.40 [skip ci] ([1e69812](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1e69812c565ea081d64b79a1a4e50cf53d3255aa))

## [1.0.40](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.39...1.0.40) (2025-03-22)

### Dependency updates

* **core-deps:** update collektive to v17.1.2 ([a31c1b4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a31c1b4f24c4bef8b1060ecfeaaedd2e82785b39))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.39 [skip ci] ([4978ff5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4978ff56807a96fd66f1148cbb64e9a3818357a7))

## [1.0.39](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.38...1.0.39) (2025-03-22)

### Dependency updates

* **core-deps:** update collektive to v17.1.1 ([192c76c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/192c76cf630a1cc575b116c63f63d33bd06f1794))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.38 [skip ci] ([abdf17e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/abdf17e4f8e6094e0d7e7242f4495577d5a989de))

## [1.0.38](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.37...1.0.38) (2025-03-21)

### Dependency updates

* **core-deps:** update collektive to v17.1.0 ([9832f74](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9832f74f8db8d0c8cbbf98256367b8c38fb75856))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.37 [skip ci] ([897f5c0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/897f5c0d5b529b979f667464a83d44b9abf928c2))

## [1.0.37](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.36...1.0.37) (2025-03-21)

### Dependency updates

* **core-deps:** update collektive to v17.0.2 ([6ad4d9a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6ad4d9af88c00f6ec6c060e35828d737034e7f6c))

### Build and continuous integration

* **deps:** update actions/download-artifact action to v4.2.0 ([8aa8e89](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8aa8e894bf43d99127137066bd62ca7b4d295c8b))
* **deps:** update actions/download-artifact action to v4.2.1 ([f753ca1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f753ca1a10aacbccccf6b4231823ee52f98d425b))
* **deps:** update actions/upload-artifact action to v4.6.2 ([09110d2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/09110d2a62633dd170b755d836c074c1073956af))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.13 ([501fdc5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/501fdc51c6f1ef04273eb85f1c6342938a80e3f2))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.36 [skip ci] ([68dfb54](https://github.com/Collektive/collektive-experiments-bootstrap/commit/68dfb547917620e8977f8c703dd4a4667b1ee408))

## [1.0.36](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.35...1.0.36) (2025-03-17)

### Dependency updates

* **core-deps:** update collektive to v17.0.1 ([86cbe0e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/86cbe0e315749ff6b7a59606351c5bf9e63d7423))

### Build and continuous integration

* **deps:** update actions/setup-node action to v4.3.0 ([4f75b01](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4f75b018226c25992281641daa173e258e30e487))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.35 [skip ci] ([7467263](https://github.com/Collektive/collektive-experiments-bootstrap/commit/74672631728c7eaaeb2fc095f9c5ccb749c86ec8))

## [1.0.35](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.34...1.0.35) (2025-03-16)

### Dependency updates

* **core-deps:** update collektive to v17 ([01a0a58](https://github.com/Collektive/collektive-experiments-bootstrap/commit/01a0a58ba109554bbdeb0420bf1bf28327bc62b4))
* **deps:** update alchemist to v39.0.1 ([c9adeba](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c9adeba08efc310fac1574bbdf8044a9ad131cee))
* **deps:** update alchemist to v40 ([018bc5a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/018bc5a6407e845eb39a8d30f478984ed77d0d56))
* **deps:** update alchemist to v40.1.2 ([df38fc2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/df38fc20bc12ab176958b2faa6a5407a589fbe1c))
* **deps:** update alchemist to v40.1.3 ([2daa4b7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2daa4b7d8ac19edbf52fc6d63d7d103ec69a417e))
* **deps:** update alchemist to v41 ([b70cff1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b70cff1cfba9191c4efb0fcd1fc608a82f855bd5))
* **deps:** update alchemist to v42 ([3db490a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3db490add620cfe119b24e898e8fff2e08162dc4))
* **deps:** update alchemist to v42.0.1 ([a9239ba](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a9239ba216de7bf6eca21580e3cd624ba8c58526))
* **deps:** update dependency gradle to v8.13 ([9082f83](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9082f835ed6329c1f9afac20946dbe3d7b42228c))
* **deps:** update dependency matplotlib to v3.10.1 ([c2b2c18](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c2b2c18f2f6f012d5c323f37928365ba4195b6f7))
* **deps:** update plugin multijvmtesting to v3.2.3 ([8f7f4df](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8f7f4df61d4c795848db1c5f0b7341aa2d6a22af))
* **deps:** update plugin tasktree to v4.0.1 ([be17d9c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/be17d9cc8e03e32a63854de56dfbd53689c70b82))

### Build and continuous integration

* **deps:** update actions/download-artifact action to v4.1.9 ([45d7cbe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/45d7cbe7b0a7495993695724cb8ff531ef3c0116))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.11 ([8b9ec48](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8b9ec48f5dd0cd1f8210d978b9e90cd272d0bb35))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.12 ([b5d2c4d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b5d2c4d30439c9cf78171d577860ce214a1d4cd1))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.34 [skip ci] ([6ad80d6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6ad80d620a9036c7a8823f46a766497f00068606))

## [1.0.34](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.33...1.0.34) (2025-02-22)

### Dependency updates

* **core-deps:** update collektive to v16.1.1 ([6463a68](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6463a683f9d1e460aa1d33a467cc5be93807c753))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.125 ([a14ad2a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a14ad2a7bbe72902b67997c2a5bfe6b6eef0724d))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.33 [skip ci] ([f7f5b5e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f7f5b5eb4d3ef892eb55763c3a25f33261c0fd21))

## [1.0.33](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.32...1.0.33) (2025-02-21)

### Dependency updates

* **core-deps:** update collektive to v16.1.0 ([47d94b9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/47d94b997610dd893fca3081c6333452699df0e8))
* **deps:** update alchemist to v38.0.1 ([76760d2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/76760d2feacd780c862f0a07b5cd0fc076c80997))
* **deps:** update alchemist to v38.0.2 ([8793c1c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8793c1c7f712fd4e4ca4a33520848599a82766da))
* **deps:** update alchemist to v39 ([cd155e5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cd155e562e007d8dfa9b679d6cad62033ba2e216))
* **deps:** update alpine docker tag to v3.21.3 ([d50c995](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d50c995934edd8e70a4c54b9233e20a43557ab6e))
* **deps:** update dependency it.unibo.alchemist:alchemist-swingui to v38.0.3 ([de98c96](https://github.com/Collektive/collektive-experiments-bootstrap/commit/de98c967752ee79cb1a96af35a2a167825264303))
* **deps:** update plugin com.gradle.enterprise to v3.19.2 ([f6f150f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f6f150f33b2d17981816d9fd32519e9c3b3a795e))

### Build and continuous integration

* **deps:** update actions/upload-artifact action to v4.6.1 ([66618d5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/66618d5742335ef5624e3ddd88c3da41fefe9927))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.10 ([6eeff8a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6eeff8a0a8f045f7a43bac03b8e66f5d76ad0d19))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.9 ([480bc12](https://github.com/Collektive/collektive-experiments-bootstrap/commit/480bc12ddc7bbb8691be0f1a614232cb3173df81))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.32 [skip ci] ([c315dd5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c315dd50a008b7a605ea5ce774007ed67fdfe5dd))

## [1.0.32](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.31...1.0.32) (2025-02-16)

### Dependency updates

* **core-deps:** update collektive to v16.0.1 ([9f863f3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9f863f30c3a795651932b0bf4897619462c9d563))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.123 ([fdd77df](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fdd77df645fc58d47d5ce25f032f6334b40bab05))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.124 ([2fe2171](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2fe21719695defe735f6136aea0fa0c6c2d774c4))
* **deps:** update node.js to 22.14 ([f63cf67](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f63cf67ab505482f658c154f77c435204840f6cc))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.31 [skip ci] ([81a2041](https://github.com/Collektive/collektive-experiments-bootstrap/commit/81a204108696ebc145a0d79df37bff0e4d036ad7))

## [1.0.31](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.30...1.0.31) (2025-02-12)

### Dependency updates

* **core-deps:** update collektive to v16 ([d6720b7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d6720b7e1dc17974800e8deb77974b7b6e4604fc))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.30 [skip ci] ([b982a6c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b982a6c9323990a23c5356540f2c764d3c5b2798))

## [1.0.30](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.29...1.0.30) (2025-02-11)

### Dependency updates

* **core-deps:** update collektive to v15 ([cbe8794](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cbe8794fb0ae02820d039345bfde84fb8fa9bedf))
* **deps:** update alchemist to v37.3.1 ([e6cbac8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e6cbac878b9454b0724138a943a17bf4accc11b6))
* **deps:** update alchemist to v38 ([bf76364](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bf763640995ba57e09b971668d12d07860bbbcbd))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.29 [skip ci] ([b69dcb2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b69dcb2a80819640bdd233e5e2188c9ac8d9a9e0))

## [1.0.29](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.28...1.0.29) (2025-02-10)

### Dependency updates

* **core-deps:** update collektive to v14 ([70556f0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/70556f07716c9a281952212738a5b4674259f98b))
* **deps:** update alchemist to v37.1.7 ([797fccb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/797fccbff4a36b86fda096a733fcf7e4b9267fd2))
* **deps:** update alchemist to v37.1.8 ([9a8e0ca](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9a8e0cac49b969740c4713370ff187fce5b3be25))
* **deps:** update alchemist to v37.2.0 ([1c35d42](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c35d42eba6f5fafefe4d7604c161299cd25bf58))
* **deps:** update alchemist to v37.2.1 ([a8a600b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a8a600b2dbbec235a2dfac3b34c43c485ff804f2))
* **deps:** update alchemist to v37.3.0 ([ff0f50a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ff0f50a290742887d60a6c75ee653bc09f0f658c))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.120 ([ee5e59e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ee5e59ecbec3f01b7f77da7c2ea520cd301a51bf))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.122 ([8a3378c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8a3378c0adbb1c8298c3a0825a9b7e2330b30ca1))
* **deps:** update dependency xarray to v2025.1.2 ([54da7cd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/54da7cd0ad1d189e89a9e409a72d2a612cdf9f75))
* **deps:** update python docker tag to v3.13.2 ([3b58498](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3b58498b187d529d184d10e1870ff4b1d212c6b3))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.28 [skip ci] ([5ead549](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5ead549749ee2b91e0d03712a96f5bff24dad3af))

## [1.0.28](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.27...1.0.28) (2025-02-01)

### Dependency updates

* **core-deps:** update collektive to v13.1.1 ([0f1daf5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0f1daf550160473cef0c8318dffe8bdc09fb63dd))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.8 ([a749a51](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a749a51416b3ee22fa6705b30293ec6efbb8a891))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.27 [skip ci] ([0638333](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0638333e8a7981c0e40ea2ef07487e78264f76b6))

## [1.0.27](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.26...1.0.27) (2025-01-30)

### Dependency updates

* **core-deps:** update collektive to v13.1.0 ([faa34a9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/faa34a9662ee73e873b1e8445bb705967f112321))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.26 [skip ci] ([7e17fb6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7e17fb655d7693f41b9a4a6d518098a7d1be5cfa))

## [1.0.26](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.25...1.0.26) (2025-01-29)

### Dependency updates

* **core-deps:** update collektive to v13 ([a5c676b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a5c676b65a08ff18619aa76c7cf1a660644845d4))
* **deps:** update alchemist to v37.1.6 ([5690b8d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5690b8d13292563bc2810a9ff919e174f9614a53))
* **deps:** update plugin gitsemver to v4.0.2 ([1e20ad1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1e20ad1529cf526a18879ed600e636a7fce91755))

### Build and continuous integration

* **deps:** update actions/setup-python action to v5.4.0 ([83f0320](https://github.com/Collektive/collektive-experiments-bootstrap/commit/83f032036316e9c0e8389ccf095867ca7e0fc1c6))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.7 ([754554a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/754554ab09105ed057f820fa70641d58830d7865))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.25 [skip ci] ([3721608](https://github.com/Collektive/collektive-experiments-bootstrap/commit/37216084b02e3abe2960c231f5f085c291a608e2))

## [1.0.25](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.24...1.0.25) (2025-01-27)

### Dependency updates

* **core-deps:** update dependency it.unibo.collektive.collektive-plugin to v12.3.3 ([69ce108](https://github.com/Collektive/collektive-experiments-bootstrap/commit/69ce1087cc87d73fe36e78f71fd9c4e3c819b1a1))
* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.1.10 ([480657b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/480657b72c6138fd7f4d5e7734a329bc1c0cc089))
* **deps:** update plugin gitsemver to v3.1.10 ([3f30870](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3f308702f4c8161b42d0f6e21657b186ddc4538d))
* **deps:** update plugin gitsemver to v3.1.9 ([722b294](https://github.com/Collektive/collektive-experiments-bootstrap/commit/722b294434ead8cdd480cc5d78a37e87a46ca5f4))
* **deps:** update plugin gitsemver to v4 ([f1f6650](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f1f66508f680c3c44a8fba8d3b5e2e1a7eddca46))
* **deps:** update plugin multijvmtesting to v3.2.2 ([429278e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/429278ebaf9c363065cb93cc28a372dc7fb4b65f))

### Build and continuous integration

* **deps:** update actions/setup-node action to v4.2.0 ([fa12f8e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fa12f8e55cbc954a8eba0eef3210c5f5e1e5df30))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.24 [skip ci] ([50418e3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/50418e3a497f0f20771bf91994c0f62f94ca6fb0))

## [1.0.24](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.23...1.0.24) (2025-01-26)

### Dependency updates

* **core-deps:** update collektive to v12.3.1 ([462480f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/462480fbcfedb928bfae502560bfbc1316222947))
* **deps:** update alchemist to v37.1.1 ([19f0d2a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/19f0d2ab311024271ac590c80b96dcc10dcbdf06))
* **deps:** update alchemist to v37.1.2 ([1c91bab](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1c91babaaf2482770a581efd02c294b4830a0bee))
* **deps:** update alchemist to v37.1.3 ([e32fb84](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e32fb84b627b22897fa0c8302515c9c7a041fe1f))
* **deps:** update alchemist to v37.1.4 ([f8cd8e8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f8cd8e82895702abf07ea5e6c0b921535b25625f))
* **deps:** update alchemist to v37.1.5 ([9e360eb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9e360ebe18b5e0277d47b7d9da1bf97733965536))
* **deps:** update dependency gradle to v8.12.1 ([5c118a7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5c118a73a93106f1b6d5f6aa12bb692ab82adb76))
* **deps:** update plugin com.gradle.enterprise to v3.19.1 ([b52fcbb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b52fcbb4db933253f16a771b1bb5c25abb598a12))
* **deps:** update plugin gitsemver to v3.1.8 ([4013439](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4013439386d462ab1457e467f8f9819cdcf8a5a5))
* **deps:** update plugin multijvmtesting to v3.2.0 ([6ac99e3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6ac99e344dca25769b5c3186dac7f8738b647247))
* **deps:** update plugin multijvmtesting to v3.2.1 ([d8450ce](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d8450ce31db7e2f13d2c5d6e89cc4dcacb9f034a))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.1 ([3b24e26](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3b24e263082b15f236c6e7236bae8c518f10101c))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.2 ([2f63d35](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2f63d35b2417e0735804f92660343e589b40c633))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.3 ([5d7f65f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5d7f65fd02409c80d067ad26b93f0600dac609dc))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.5 ([cf0a5ea](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cf0a5eac3a382cc46d4240a482f7b4e2cf157f4d))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.6 ([9f7cae4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9f7cae4b034448e3b753596efa68cc418b7fa3fe))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.23 [skip ci] ([4cd8653](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4cd865375dcb19e94ed87e3e126fc853e77e57dc))

## [1.0.23](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.22...1.0.23) (2025-01-20)

### Dependency updates

* **core-deps:** update collektive to v12.3.0 ([e0086a5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e0086a5f437cdab4e1f70537431a8674fc8b4fd5))
* **deps:** update alchemist to v37.1.0 ([ff8ae72](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ff8ae720d9f9572d5a2107c9f9892a8e66b978b9))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.22 [skip ci] ([ad1531b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ad1531bef2b072f4edc45c8a3c4e7b5274f95d70))

## [1.0.22](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.21...1.0.22) (2025-01-19)

### Dependency updates

* **core-deps:** update collektive to v12.2.2 ([a15f367](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a15f36764df25f7322d6717f8ebc89c3e092bcb3))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.21 [skip ci] ([9735586](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9735586658fb355f05bc13d869c9242e78d0f6b7))

## [1.0.21](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.20...1.0.21) (2025-01-18)

### Dependency updates

* **core-deps:** update collektive to v12.2.1 ([d09689f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d09689fd0f5f57aef1d7cb5c040b9e4e39f7fd49))
* **deps:** update alchemist to v37.0.1 ([83b4010](https://github.com/Collektive/collektive-experiments-bootstrap/commit/83b4010ec8ec7a0347c770f2a767d4381780180e))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.20 [skip ci] ([1d6e8ed](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1d6e8ed20a97c9fad581ef5a5aebf9178c7e6b1d))

## [1.0.20](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.19...1.0.20) (2025-01-17)

### Dependency updates

* **core-deps:** update collektive to v12.2.0 ([0214719](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0214719c5247765e83164c8af499f2e938e36582))
* **deps:** update alchemist to v37 ([4e294ad](https://github.com/Collektive/collektive-experiments-bootstrap/commit/4e294ad49f7582393091d753964ae5677e4c284d))
* **deps:** update dependency xarray to v2025.1.1 ([f56c61a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f56c61a292c7d2e8a77c710d4c0b5a3f2d112243))

### Build and continuous integration

* **deps:** update actions/upload-artifact action to v4.6.0 ([05781e7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/05781e7dae840e2b453414f130aa1b41a9710981))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.19 [skip ci] ([ffb1b09](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ffb1b097a471cea29d591f30bcadbd1bd215689e))

## [1.0.19](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.18...1.0.19) (2025-01-10)

### Dependency updates

* **core-deps:** update collektive to v12.1.1 ([7710dbe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7710dbe9fa594c341e13b81dff3caca9d0001fd2))
* **deps:** update alchemist ([a2b1460](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a2b146073e1563665474a3d4e1534f166147a91c))
* **deps:** update alchemist to v36.1.3 ([9c82f5b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9c82f5b1ad759452b3d16f1ff5aaafeb579a0c0a))
* **deps:** update alpine docker tag to v3.21.1 ([3d6094f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3d6094f06e9fc63ed8a6399f09fc4a46e490fe11))
* **deps:** update alpine docker tag to v3.21.2 ([f6f8bc1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f6f8bc1adbe1985dc673b2e07c8b47d910887096))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.7.0 ([b71ded9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b71ded97d43d24e73774e133451ee2cf553a6f86))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.18 [skip ci] ([db8ad21](https://github.com/Collektive/collektive-experiments-bootstrap/commit/db8ad21f1e476fa2a80d4fc290906351724b2da7))

## [1.0.18](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.17...1.0.18) (2025-01-09)

### Dependency updates

* **core-deps:** update collektive to v12.0.3 ([774c236](https://github.com/Collektive/collektive-experiments-bootstrap/commit/774c2369fb698ca245bf5c740f01ea59102af80e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.118 ([6e7eef1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6e7eef1d59c72a41011b0205b9eb4c593659444b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.119 ([64bdc12](https://github.com/Collektive/collektive-experiments-bootstrap/commit/64bdc12431cdc9acf439a054e765840869ae2af7))
* **deps:** update node.js to 22.13 ([00a6437](https://github.com/Collektive/collektive-experiments-bootstrap/commit/00a6437e5c97a729eeb24f88c4abb089e4491389))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.17 [skip ci] ([30a5a82](https://github.com/Collektive/collektive-experiments-bootstrap/commit/30a5a8213aaacc49adcdc55780e54041c3e97e31))

## [1.0.17](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.16...1.0.17) (2025-01-08)

### Dependency updates

* **core-deps:** update collektive to v12.0.2 ([cc396c1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cc396c11fc0ff9cd87126b6d2eba4bd79ad8d34f))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.16 [skip ci] ([0ff9dad](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0ff9dad0464e4632976c28835137d6f3b750a275))

## [1.0.16](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.15...1.0.16) (2025-01-08)

### Dependency updates

* **core-deps:** update dependency org.jetbrains.kotlin.jvm to v2.1.0 ([974a700](https://github.com/Collektive/collektive-experiments-bootstrap/commit/974a700951984384c37fea527072eab72a548921))
* **deps:** update plugin multijvmtesting to v3 ([83b58c0](https://github.com/Collektive/collektive-experiments-bootstrap/commit/83b58c0e69c2083fad0ba4a231703ebef256f887))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.15 [skip ci] ([b00df8a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b00df8aa7be86f6ac0baa838d83709fcd635d8df))

## [1.0.15](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.14...1.0.15) (2025-01-08)

### Dependency updates

* **core-deps:** update collektive to v12.0.1 ([d88891d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d88891de2ceba461c991ee63edf89375a783534a))
* **deps:** update dependency xarray to v2025 ([d21467e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d21467ecb7e9620092c6ec21b6b0786cea86896c))
* **deps:** update plugin kotlin-qa to v0.77.1 ([88f53de](https://github.com/Collektive/collektive-experiments-bootstrap/commit/88f53de7700192c7201371e62446c669e6851c04))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.14 [skip ci] ([f63e299](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f63e299e6e83982d5e9da50d1aa81298ea945297))

## [1.0.14](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.13...1.0.14) (2024-12-28)

### Dependency updates

* **core-deps:** update collektive to v12 ([cfffa9b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cfffa9b65dd6731d81691804e0820082bc250659))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.13 [skip ci] ([430ce90](https://github.com/Collektive/collektive-experiments-bootstrap/commit/430ce90dfb8edabc15ef20346c2a6754c9989cfd))

## [1.0.13](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.12...1.0.13) (2024-12-24)

### Dependency updates

* **core-deps:** update collektive to v11.2.0 ([d56fdbf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d56fdbf53e79db6304fb0cca589856c43c0eb022))
* **deps:** update alchemist to v36.0.12 ([18e42c7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/18e42c75a15ad9b19c092fa00239fb22be35b56e))
* **deps:** update dependency gradle to v8.12 ([ab2f006](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ab2f0065bcd04f8d50eedc07ae1523663ec476d4))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.117 ([1ed022b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1ed022b119dbdac045cd1a227b776ee9ea61f991))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.12 [skip ci] ([23f080b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/23f080b9d9a5fc91e5c1e74924ef1ca12019fe54))

## [1.0.12](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.11...1.0.12) (2024-12-20)

### Dependency updates

* **core-deps:** update collektive to v11.1.3 ([995d148](https://github.com/Collektive/collektive-experiments-bootstrap/commit/995d148ae30763c92e75cf924e86d0a968367174))
* **deps:** update alchemist to v36.0.10 ([401bd18](https://github.com/Collektive/collektive-experiments-bootstrap/commit/401bd1879d0ea203cb4f03faa2691afd7506a33e))
* **deps:** update alchemist to v36.0.11 ([1bdad76](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1bdad761515bd730853ce5dc84246504a5dc67eb))
* **deps:** update alchemist to v36.0.7 ([595e3fa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/595e3fab262741f81d8ad440d23672724b901429))
* **deps:** update alchemist to v36.0.9 ([ecb6ace](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ecb6ace55efac592410139a1d4c77568ce944005))
* **deps:** update dependency it.unibo.alchemist:alchemist to v36.0.8 ([0c35bff](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0c35bff7a682207fcd4ad974d1e2de783b19471b))
* **deps:** update dependency matplotlib to v3.10.0 ([9f47e5d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9f47e5dbcc1c4db9c72b997fd423f034792837fb))
* **deps:** update dependency matplotlib to v3.9.4 ([8d8f1c1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8d8f1c10676c1919461691a1352210e0fdddad03))
* **deps:** update plugin com.gradle.enterprise to v3.19 ([2c39770](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2c39770a62076530d509420652596948ce920446))

### Build and continuous integration

* **deps:** update actions/upload-artifact action to v4.5.0 ([7553e15](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7553e15e4bec06aab9a4306cef49d0f7afa3d825))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.26 ([f02019b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f02019bdefffaf2a321cb2588e27df1aa8a0f311))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.27 ([42f2209](https://github.com/Collektive/collektive-experiments-bootstrap/commit/42f2209a80dc33216fce5f6954d23e25bf42ea83))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.28 ([14d1287](https://github.com/Collektive/collektive-experiments-bootstrap/commit/14d128730c843cca42f2e978084b8ec51eeb1236))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.11 [skip ci] ([e76c918](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e76c91888a0760ace6fe4adcc45aaf1c728391a8))

## [1.0.11](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.10...1.0.11) (2024-12-10)

### Dependency updates

* **deps:** update alchemist to v36.0.4 ([5523061](https://github.com/Collektive/collektive-experiments-bootstrap/commit/55230617d81bdc29beb7c75de01a1cbf7848abb7))
* **deps:** update alchemist to v36.0.5 ([83c5e4d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/83c5e4df652fa1a5e514c968346deaac64ad618a))
* **deps:** update alchemist to v36.0.6 ([6b2bebc](https://github.com/Collektive/collektive-experiments-bootstrap/commit/6b2bebce98671046de2c8f90ebf626c286e5f776))
* **deps:** update alpine docker tag to v3.21.0 ([8f1839c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8f1839ce4e75a9d6e31b3df2dd6ed7f95f0d36a3))
* **deps:** update dependency matplotlib to v3.9.3 ([350802c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/350802c73e2645e576f6ffed2f2143fa6ad96e6e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.116 ([89ec2d3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/89ec2d3a8f66021a5b64d3fe187c3632719e8a50))
* **deps:** update node.js to 22.12 ([d014993](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d01499348ef82fd0f0ae676c2e04f9557bc11299))
* **deps:** update plugin kotlin-qa to v0.77.0 ([f5cb66b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f5cb66bc7bc744da83bed7462b2f15b2b3d5d420))
* **deps:** update plugin multijvmtesting to v2 ([2918a84](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2918a84124fcffc3cc344acc25f2daf470e206ad))
* **deps:** update python docker tag to v3.13.1 ([172612f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/172612fff025e96087c562bf4675aaabe4dd4be8))

### Bug Fixes

* remove use of context receivers ([8a9e3a7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8a9e3a73774f998f2461977dd45d1c0509ea9190))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.24 ([5e70ee9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5e70ee92eaec282cdb2eb1f212579ccfa3e3a9e7))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.25 ([25aef25](https://github.com/Collektive/collektive-experiments-bootstrap/commit/25aef25d04a03c9606f735f660549fb19c66fb46))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.10 [skip ci] ([bb0eba9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bb0eba94c3b123dae6bd4b3c4bc45a37553f09ae))

## [1.0.10](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.9...1.0.10) (2024-12-02)

### Dependency updates

* **core-deps:** update collektive to v11.0.2 ([c233565](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c233565ae5b90fbe6c0a4ce06f3f2436544fda33))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.9 [skip ci] ([262148b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/262148bb8c3fcb0f8d966ad1bba19e29ee041300))

## [1.0.9](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.8...1.0.9) (2024-12-02)

### Dependency updates

* **core-deps:** update collektive to v11.0.1 ([9f8972b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9f8972bf5e9a991516801560b2fcc39efe137c56))
* **deps:** update alchemist to v35.0.3 ([fa18edf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fa18edf5f28c440669683dd8446b0e8ea01c2b4b))
* **deps:** update alchemist to v36.0.1 ([7fab60c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7fab60c3ce44f64f544ce76ae85002fb18653131))
* **deps:** update alchemist to v36.0.2 ([38c2bf1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/38c2bf1085a74867e460068c7e1320a4b4ec6fd8))
* **deps:** update alchemist to v36.0.3 ([3e3db05](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3e3db05208c8508f31c6ae42a4b0e73c21ffe5ec))
* **deps:** update dependency gradle to v8.11 ([0aa3ffa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0aa3ffa22b300d884c1ab13876b1ee56a315f6a9))
* **deps:** update dependency gradle to v8.11.1 ([d6924e1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d6924e16a7b23c25d4142f939361a6195b525fe0))
* **deps:** update dependency it.unibo.alchemist:alchemist to v35.0.1 ([9330de3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9330de36ad11aa92f06a9f9e6f09f0a91ca0f254))
* **deps:** update dependency it.unibo.alchemist:alchemist-euclidean-geometry to v35.0.2 ([81e43cd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/81e43cd2226f64e24a635ec782a7cfbd12856982))
* **deps:** update dependency it.unibo.alchemist:alchemist-swingui to v36 ([002d280](https://github.com/Collektive/collektive-experiments-bootstrap/commit/002d280c7e9282ebbeb8ff1450a4865d4fc79714))
* **deps:** update dependency xarray to v2024.11.0 ([cafeb93](https://github.com/Collektive/collektive-experiments-bootstrap/commit/cafeb935f0bf5689b4ba361be498d0854670a6b1))
* **deps:** update plugin kotlin-qa to v0.70.0 ([9cf62f5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9cf62f56c3c22f289be07a394e6daddff97c5775))
* **deps:** update plugin kotlin-qa to v0.70.1 ([087920b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/087920bbd14423edde3a1fb22cba6bdada1e5520))
* **deps:** update plugin kotlin-qa to v0.70.2 ([b27fe47](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b27fe475d50f5b2645b8f265781f82238fac2006))
* **deps:** update plugin kotlin-qa to v0.71.0 ([acfc042](https://github.com/Collektive/collektive-experiments-bootstrap/commit/acfc042c6e7b79fb6352da2f68c2a69c89a409de))
* **deps:** update plugin kotlin-qa to v0.72.0 ([3adc574](https://github.com/Collektive/collektive-experiments-bootstrap/commit/3adc57472d74a25a0cd744bf605e4280c4ad92db))
* **deps:** update plugin kotlin-qa to v0.73.0 ([7caa45f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7caa45fb085b1b9154f789040da0f0238bc49922))
* **deps:** update plugin kotlin-qa to v0.74.0 ([ebe7f77](https://github.com/Collektive/collektive-experiments-bootstrap/commit/ebe7f77f7ffa122514bdf6cfc89d880ef71d91a9))
* **deps:** update plugin kotlin-qa to v0.75.0 ([78b4844](https://github.com/Collektive/collektive-experiments-bootstrap/commit/78b48441f684f913a284fc4bdb3558496f8aaea3))
* **deps:** update plugin multijvmtesting to v1.3.1 ([3878240](https://github.com/Collektive/collektive-experiments-bootstrap/commit/38782401110caf6dad4f459aab7f30ec5458b235))
* **deps:** update plugin multijvmtesting to v1.3.2 ([aa929c6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/aa929c614fe869ab1c6c91b4144928f5316edbd9))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.9.0 ([099d58e](https://github.com/Collektive/collektive-experiments-bootstrap/commit/099d58e0686db55eede27e26047ab2e305a1dd17))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.15 ([c16934d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c16934dc2caad1396f897e2fe160571f74ba9200))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.16 ([e1dfc7a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e1dfc7aa2596c742c54ad53ec5449b8f1976c080))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.17 ([e516a2d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e516a2d15118e21a5dea9170f1fc9a1c1984e83c))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.18 ([72797a1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/72797a168bf4bc53a978812839425a9f30e218e4))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.19 ([94b1960](https://github.com/Collektive/collektive-experiments-bootstrap/commit/94b19607e42e9ddbe209d21f57d71e69fc7ee4a3))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.20 ([992de78](https://github.com/Collektive/collektive-experiments-bootstrap/commit/992de789ff116ce3a653ebeae372dcd164713b95))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.21 ([7e524d5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7e524d5c0a6122e57dfe6473a0631da19b398b02))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.22 ([c57fd04](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c57fd043001283200d426504a8926206c3c9cf80))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.23 ([7d4e9c9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7d4e9c9638f6643b8d7388f8cafbb3aae1ee4915))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.8 [skip ci] ([2950bae](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2950bae88896aea6b7e84a7f8be84b1952655e5f))

## [1.0.8](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.7...1.0.8) (2024-11-14)

### Dependency updates

* **core-deps:** update collektive to v11 ([d76feaa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d76feaa7dec9800bb52a70f5cda1aef44169eac2))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.7 [skip ci] ([fb95526](https://github.com/Collektive/collektive-experiments-bootstrap/commit/fb95526c3eca6e5e113469dc91dce9999ca173d2))

## [1.0.7](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.6...1.0.7) (2024-11-14)

### Dependency updates

* **core-deps:** update collektive to v10.11.1 ([8599670](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8599670d93ed5100b8e5b5a7ef1098478d263817))
* **deps:** update alchemist to v35 ([877b9fb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/877b9fb2cbfb962a4c277fd34898e57042386125))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.115 ([5ed905b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5ed905b5788f398093493a3959d6d7bb3b7d333e))
* **deps:** update plugin com.gradle.enterprise to v3.18.2 ([dc7bfad](https://github.com/Collektive/collektive-experiments-bootstrap/commit/dc7bfad1021e0f2dea1194b0e1b772414e629288))

### Build and continuous integration

* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.13 ([e26d888](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e26d8880da8bba17cf77979e5169bf34e2eeb7e8))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3.5.14 ([14d8d80](https://github.com/Collektive/collektive-experiments-bootstrap/commit/14d8d802b7cc689ea64eedd1f067f58b2b9dcfd2))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.6 [skip ci] ([d7ac766](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d7ac766a9bb04c1c0c9ef4c02c5f2500ae131780))

## [1.0.6](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.5...1.0.6) (2024-11-11)

### Dependency updates

* **core-deps:** update collektive to v10.11.0 ([e891a8a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e891a8adc4c3e4f809c81ceb2d20e65a44c8f24f))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.5 [skip ci] ([db4bdb1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/db4bdb13ea7780bce2a4e52799e26143dca9ca02))

## [1.0.5](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.4...1.0.5) (2024-11-10)

### Dependency updates

* **core-deps:** update collektive to v10.10.0 ([8572868](https://github.com/Collektive/collektive-experiments-bootstrap/commit/85728688abb81f3c14d0b1a103d3c99ee73978bf))
* **deps:** update alchemist to v34.1.13 ([f906a8d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f906a8d02b0e5e9b101918bfe49eb6988f0e814a))
* **deps:** update alchemist to v34.1.14 ([9a90fcb](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9a90fcb7f685e29f0e508c719ff1a9f1696efe1f))
* **deps:** update plugin multijvmtesting to v1.3.0 ([8f7fa59](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8f7fa5936c894626666d357d9d1016db599078d1))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.4 [skip ci] ([17fcce3](https://github.com/Collektive/collektive-experiments-bootstrap/commit/17fcce38f182ef4e3d1b2698adbad4d4783c8790))

## [1.0.4](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.3...1.0.4) (2024-11-08)

### Dependency updates

* **core-deps:** update collektive to v10.9.0 ([f12aae5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f12aae5f17c3dcd59136b81fbc32bf6975ba865f))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.3 [skip ci] ([30b8da6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/30b8da6d84fcab8d95379f9139dafb8af1a048ac))

## [1.0.3](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.2...1.0.3) (2024-11-07)

### Dependency updates

* **core-deps:** update collektive to v10.8.0 ([1ae6ee5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1ae6ee5d0eac1d42583143442036db6f9b8030d2))

### General maintenance

* **release:** update gradle.properties .env versions to 1.0.2 [skip ci] ([c05af76](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c05af76192a6d181bbce5aa69d7d913334f192a0))

## [1.0.2](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.1...1.0.2) (2024-11-06)

### Dependency updates

* **core-deps:** update collektive to v10.7.0 ([8f5d5e8](https://github.com/Collektive/collektive-experiments-bootstrap/commit/8f5d5e8924e29fc14cd2da5214a5c6f9a7e30921))
* **deps:** update alchemist to v34.1.10 ([d96087c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d96087c8daa7383e74c52499f08f3327d390a5da))
* **deps:** update alchemist to v34.1.11 ([b137cf2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b137cf265f7c7543e74ab5106c9dcf062ad23d05))
* **deps:** update alchemist to v34.1.12 ([bb9a493](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bb9a493307457b2605755643ea360b593c2f8029))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v2.0.21 ([1b3cb30](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1b3cb30fbf4f7b9b70f539f5f400334d110aed34))
* **deps:** update plugin gitsemver to v3.1.7 ([f0e029a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f0e029af7f4f8e7038bde0cec39803f58408ab15))
* **deps:** update plugin kotlin-qa to v0.69.0 ([81e7a8b](https://github.com/Collektive/collektive-experiments-bootstrap/commit/81e7a8b4e7f98db13bb0a115f91a718954be0bdb))
* **deps:** update plugin multijvmtesting to v1 ([5bdf9cf](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5bdf9cf612e36fb1f3834eef9a27995b9718ba4a))
* **deps:** update plugin tasktree to v4 ([2ec0204](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2ec020468a137a06912b50961a475387af459bfb))

### Bug Fixes

* follow Collektive's renovate configuration ([bb247fd](https://github.com/Collektive/collektive-experiments-bootstrap/commit/bb247fd3aeaa64dded39db89271cae531a4dbc5e))

### Build and continuous integration

* **deps:** update actions/checkout action to v4.1.7 ([5b0f1f1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5b0f1f191a627c81235e33ac9c7dd5cf1d9ed652))
* **deps:** update actions/checkout action to v4.2.2 ([9d06826](https://github.com/Collektive/collektive-experiments-bootstrap/commit/9d0682623e87545a6aa569e23b1579ca6896fb63))
* **deps:** update actions/download-artifact action to v4.1.8 ([82fbdb7](https://github.com/Collektive/collektive-experiments-bootstrap/commit/82fbdb7b377069948ce56d04ab047bf58e0d88bf))
* **deps:** update actions/setup-python action to v5.1.1 ([241df63](https://github.com/Collektive/collektive-experiments-bootstrap/commit/241df63715742f20ed5b9e89520c188d6a9e8b59))
* **deps:** update actions/setup-python action to v5.3.0 ([48d8c40](https://github.com/Collektive/collektive-experiments-bootstrap/commit/48d8c403365b376a36a95e8f66a61fe9422a9cf3))
* **deps:** update actions/upload-artifact action to v4.3.6 ([c77d8ab](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c77d8ab72ca13058bd72ce2916cde3d437deea9f))
* **deps:** update actions/upload-artifact action to v4.4.3 ([53f7c8d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/53f7c8d56f7d8f1a615ca23d09c61b1d90dc872c))
* **deps:** update danysk/build-check-deploy-gradle-action action to v3 ([75ccc17](https://github.com/Collektive/collektive-experiments-bootstrap/commit/75ccc17ca508fe2da81cd1e54f6bf86b2f30d66d))
* **deps:** update dependency ubuntu github actions runner to v24 ([c4ce0e5](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c4ce0e525ca33b73bd3dc52e3c71e31a39d24418))

### General maintenance

* **build:** remove kotlin reflection depencency ([68d871d](https://github.com/Collektive/collektive-experiments-bootstrap/commit/68d871d5a8b9c22d0853bf03902c85baf381aa81))
* **release:** update gradle.properties .env versions to 1.0.1 [skip ci] ([5443806](https://github.com/Collektive/collektive-experiments-bootstrap/commit/54438063a9e266f111779fa79824fd7134da5903))

## [1.0.1](https://github.com/Collektive/collektive-experiments-bootstrap/compare/1.0.0...1.0.1) (2024-11-05)

### Dependency updates

* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.112 ([210872a](https://github.com/Collektive/collektive-experiments-bootstrap/commit/210872a0d2c240e70b1941143c2869ae1f01313c))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.113 ([e508d83](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e508d8322cf2b2611d35190fc5e3152ef1ff267c))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.114 ([7be1b72](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7be1b728117d45ee615b3140f209ee2a1aec20c3))
* **deps:** update dependency xarray to v2024.10.0 ([f1d4369](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f1d4369a3380b57f91cdc3fae8b5c76daa629c73))
* **deps:** update node.js to v22 ([b0d3b60](https://github.com/Collektive/collektive-experiments-bootstrap/commit/b0d3b60bc54a8cf1b097152b673768e99cb14edf))

### Bug Fixes

* remove warnings as errors ([754cf0f](https://github.com/Collektive/collektive-experiments-bootstrap/commit/754cf0ffd94d63e3a5b940c5d001de49a5109e93))
* silent Alchemist verbosity ([5a5fabe](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5a5fabe53821445c79f979b0392808f9099e56e6))

### Build and continuous integration

* **deps:** update actions/setup-node action to v4.1.0 ([e101e6c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e101e6c3b49a5761332957579717393e8bde152f))

### General maintenance

* **libs:** update collektive version ([f0b9cb4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f0b9cb46e3d2a432c48956601d55694afa6abfb2))
* **release:** update gradle.properties .env versions to 1.0.0 [skip ci] ([f32e182](https://github.com/Collektive/collektive-experiments-bootstrap/commit/f32e18263ff85324806026fdcfebecae86a5b747))

## 1.0.0 (2024-10-23)

### Features

* add gradient simulation example ([40dcbe2](https://github.com/Collektive/collektive-experiments-bootstrap/commit/40dcbe2c3e81cf2464f2849954369ee8a5c41134))

### Bug Fixes

* **gitGuardian:** remove useless .env ([011650c](https://github.com/Collektive/collektive-experiments-bootstrap/commit/011650c0ab8d3110ac756faf05aa832fb14735d4))
* operator plus import ([1ea39aa](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1ea39aac50a83ac2dde4117c6af3c08e39ceb4fd))
* use fielded double plus ([296cede](https://github.com/Collektive/collektive-experiments-bootstrap/commit/296cede4ccc945df371fc857a6152f7b79878c13))

### Build and continuous integration

* temporary remove login to dockerhub ([e07a230](https://github.com/Collektive/collektive-experiments-bootstrap/commit/e07a2308a91d19868a9d7c0fe904e22d398cfc08))

### General maintenance

* add .env to gitignore ([a6964f4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/a6964f439d9aea2c930c14261c7bc12a5fb42338))
* add effects for gradient simulation example ([7460369](https://github.com/Collektive/collektive-experiments-bootstrap/commit/7460369ade81657bdb181e39a23e5912a816749e))
* **build:** update build gradle with Collektive libraries ([c335630](https://github.com/Collektive/collektive-experiments-bootstrap/commit/c33563012c8943dfc2931a5127d5c2387bd3162d))
* **ci:** temporary comment task 'check simulations docker' ([1e50bf1](https://github.com/Collektive/collektive-experiments-bootstrap/commit/1e50bf114672b105e5d3b0996c9144d7f1016dba))
* fix rootproject name ([5727ea4](https://github.com/Collektive/collektive-experiments-bootstrap/commit/5727ea4c4245051fd7b4451cc53133898dbbbce3))
* **lib:** add Collektive libraries and plugin ([2f58af9](https://github.com/Collektive/collektive-experiments-bootstrap/commit/2f58af9e37a369a621cfaca21f2389615c9ba99a))
* **libs:** add collektive stdlib ([84e6d01](https://github.com/Collektive/collektive-experiments-bootstrap/commit/84e6d01a333319d511dc1df799351228b2e15aa0))
* **lib:** update kotlin version ([d93afc6](https://github.com/Collektive/collektive-experiments-bootstrap/commit/d93afc6b3282eb8b136285a5000732aa34ca7eae))
* update gitignore ([0bc0803](https://github.com/Collektive/collektive-experiments-bootstrap/commit/0bc0803a3e3d09306a91ffc102f481349b5a8066))

## [1.2.1](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.2.0...1.2.1) (2024-02-09)


### Dependency updates

* **deps:** update alchemist to v25.16.2 ([153a932](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/153a932ad1c712b2ba41304fb1c68ddff8331564))
* **deps:** update alchemist to v26 ([079e0c9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/079e0c9f44e32d2309e22946e6a89cb0afb7338b))
* **deps:** update alchemist to v26.0.1 ([aee7286](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/aee7286c958540a5c7ec846526cc2d9ed5732c04))
* **deps:** update alchemist to v26.0.10 ([8f5485e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8f5485ef904c283c9564d72ae3d2b7b3289d2dcf))
* **deps:** update alchemist to v26.0.11 ([8f584c4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8f584c45d9c577d8a9064e705c4ba29feaca7d3a))
* **deps:** update alchemist to v26.0.12 ([4a19ba6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4a19ba6b72fa51ac1a2b669b9c2a09edc4be47e1))
* **deps:** update alchemist to v26.0.13 ([22a0c75](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/22a0c7550f774babb6f27402564043f36c734357))
* **deps:** update alchemist to v26.0.2 ([0aa1060](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0aa106079ce93c7060e45a379e4b0c2062c598da))
* **deps:** update alchemist to v26.0.3 ([7b359d6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7b359d6cdf9afef92a979d181d8d0db4620a9278))
* **deps:** update alchemist to v26.0.4 ([28a633f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/28a633f5f2235458873f7fb32291699123b768c5))
* **deps:** update alchemist to v26.0.5 ([9a738a1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9a738a1e190a5bd08232c23c194d11fff1148070))
* **deps:** update alchemist to v26.0.6 ([80431b2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/80431b21faa696d3dcf6a03d6e8fd26feecff3b6))
* **deps:** update alchemist to v26.0.7 ([1a749f1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1a749f1ac5a163d9a4188fc8d7a8605418b31158))
* **deps:** update alchemist to v29 ([c537825](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c5378254ffdfa58aa30809773e9750414b21ce08))
* **deps:** update alchemist to v29.3.5 ([811e29c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/811e29ca569aa18c09f40505c0239aeaccdfe9d7))
* **deps:** update alchemist to v29.4.0 ([b94c580](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b94c580399e9e4b0aee879d2abcd8bbc1cd0ecd6))
* **deps:** update alchemist to v29.5.0 ([7290c8e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7290c8eab5120d1c0d9142a4516ee6fa4d519339))
* **deps:** update alchemist to v29.5.1 ([bc7f3d8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bc7f3d8a98e1c526b9e6b3de23a25d857747377b))
* **deps:** update alchemist to v30 (major) ([#693](https://github.com/DanySK/alchemist-experiments-bootstrap/issues/693)) ([97a25af](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/97a25af6a75e90e1c1d40a71be533ef39351feec))
* **deps:** update alchemist to v30.0.3 ([ca003b0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ca003b0e491e40a895232cf211418118de57bc53))
* **deps:** update alchemist to v30.0.4 ([94ead24](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/94ead247aa558f5c1af58232c5212cd94a23448b))
* **deps:** update alchemist to v30.0.5 ([d7a6fd0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d7a6fd0655c3f1d4bb08e2122d059e319eaf8d14))
* **deps:** update alchemist to v30.1.2 ([ff9c311](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ff9c311accadeb89355dc4df50da2451fdd2d7b9))
* **deps:** update alchemist to v30.1.3 ([b4b8848](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b4b88482773b3075eb5492b57eebb3dab967abcc))
* **deps:** update alchemist to v30.1.4 ([d6339f9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d6339f9888e11d969aeda61f6ec0b8b50f4f9778))
* **deps:** update alpine docker tag to v3.18.0 ([ac0e871](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ac0e8711b8667e99e9ba13c9deb7d4da2b61f316))
* **deps:** update alpine docker tag to v3.18.2 ([58f0bc2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/58f0bc2e83ab7154b174b5cb12df7d582cf3d4bc))
* **deps:** update alpine docker tag to v3.18.3 ([dc2b5ab](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/dc2b5abc1a2c7f291400e49c4d73c1b6f0d25439))
* **deps:** update alpine docker tag to v3.18.4 ([5059cc1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5059cc120d5e561fc1433d5984940c2279363b16))
* **deps:** update alpine docker tag to v3.18.5 ([8e805c8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8e805c8ffd729a228db8ce992d91334665373b2e))
* **deps:** update alpine docker tag to v3.19.0 ([04d3edf](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/04d3edfe2341695f16a878118540626b92eeee7a))
* **deps:** update alpine docker tag to v3.19.1 ([bef6f8f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bef6f8f1697e54ec865ab244d6fd9fab837ee463))
* **deps:** update dependency gradle to v8.2 ([487d145](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/487d1454983fef42da79e6cac067901c393e8b23))
* **deps:** update dependency gradle to v8.2.1 ([a7efd0c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a7efd0cfc81668e6714b9018c4d65fe7e131b44e))
* **deps:** update dependency gradle to v8.3 ([e8164ad](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e8164ad4b78ae646ad3e55bedd96a5f0d1665df1))
* **deps:** update dependency gradle to v8.4 ([f043d9e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f043d9ea77e545b9411c1a4e8ab0716d8dc3a194))
* **deps:** update dependency gradle to v8.5 ([4f83a98](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4f83a986ce5c6f6d0a76566466667d0b553b025e))
* **deps:** update dependency gradle to v8.6 ([4ff0a76](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4ff0a767ef99170569f2bab640aef07d36978247))
* **deps:** update dependency it.unibo.alchemist:alchemist-incarnation-scafi to v26.0.8 ([f4defbd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f4defbd197f9efdc133a8f0e54c113b5d661ae95))
* **deps:** update dependency matplotlib to v3.7.2 ([acd80b6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/acd80b6a187dc595066c55407c7ad88117acd74b))
* **deps:** update dependency matplotlib to v3.7.3 ([a83cfd9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a83cfd9ded76c09035517f078ebd1dfb2805b690))
* **deps:** update dependency matplotlib to v3.8.0 ([01f7dbb](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/01f7dbbaf54c2848fe970a1091749a73ff001577))
* **deps:** update dependency matplotlib to v3.8.1 ([2794a24](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2794a24208a896ab6f6710fd4c4f3bf580737496))
* **deps:** update dependency matplotlib to v3.8.2 ([8eb1902](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8eb19020513a6c43d979dd33083ad906123e6f24))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.8.22 ([aa2030c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/aa2030c5f9b3811c8750536a39d39b930ca6f383))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.9.0 ([65f3afe](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/65f3afe08ba42942525676656d6399879de554f9))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.9.10 ([2ed4c77](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2ed4c77ef458ac787f6876c5fc1a5290b1b47149))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.9.20 ([6f2bf6a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6f2bf6ac0d760cace65f25613a70a04f673668b4))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.9.21 ([de2a140](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/de2a1402b6516f8f03b17e910038d163f14568bb))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.9.22 ([9683dd5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9683dd595694a5f6a4c069afac7251a8802d15dd))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.27 ([fd1e295](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fd1e295c685ae9393a788c3647e5af68d965c13d))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.28 ([96438a4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/96438a441a6bc9a430380214e145c614c1db963e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.29 ([a90ff87](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a90ff8797e5b6e7693fdb90ff57c8241df2212b2))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.30 ([d68da2c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d68da2c1d531a1e13d789399f993f4c62a8692ee))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.32 ([ae5d0ad](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ae5d0addb6fdf72c0b292087b005353f5a6bc0de))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.33 ([f6a98f4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f6a98f4f3ba236d2d8743362fa46ede5cc643d95))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.34 ([7a3a3af](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7a3a3af96f6114d54a3c3caeb60970b52d38dd4a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.35 ([670b574](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/670b574e4c6d8f7b2c5c02da4d3efa8d27c8a0c1))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.36 ([d394a80](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d394a8074d7ba2bf2cd66d1c2a44dd81891a6387))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.37 ([0367dad](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0367dad9fc0e1ff47dbb7e2cc576cfc28fb8cca9))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.38 ([abf257e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/abf257eccd6ff61c86f27f56a6d5f63292f711fe))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.39 ([885ce5a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/885ce5a691f5788cbcde60fc03d673a03294cf2f))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.40 ([4f9a341](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4f9a3415f1f7b2bdbc8e7d59b350c0fec49d640a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.41 ([e2619ce](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e2619cea15b60b486f19c1d82709f2d882635959))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.42 ([a6af674](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a6af6745cc5957187d59c02d69bccb1a85c33ddc))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.43 ([c480c79](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c480c79bfae43907c826c6e08d707e22d638ef7a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.44 ([eee738d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/eee738d16a94d952ccd3221f81aa770df977c15e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.45 ([7ffb4d1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7ffb4d15884a2a18da876e684d63effa5c0306b1))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.46 ([89e9538](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/89e9538a0c01f673b1b318782889aac033dc72b2))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.47 ([3af7b30](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3af7b3014e3b49ed159cb5e655898facdb0318bf))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.48 ([0d64917](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0d649172834fc14cf101d2bb90f70471ff5fe007))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.49 ([ea84c04](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ea84c042761c84a846095df0b6ec10c2ad8ba6fe))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.50 ([3264507](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/32645078cc7539900ee7a78d2ffad3b1c27a2f1a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.51 ([8c15c05](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8c15c057e10b775f63f22d9d4c2531b3d5083404))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.52 ([943449e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/943449e455962d4beddd081f6fe3af19c7d3c92a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.53 ([6243a8d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6243a8d1e1ffe715a041bc78e3e312bf29061ff3))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.54 ([2dcb5cd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2dcb5cd78e13bfc310e04e9bcb279fbe46b7e531))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.55 ([fc2015e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fc2015e6a84e9728dc26f60162aba81588a9a606))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.56 ([de2f7f5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/de2f7f53437bfc5340e939ab395b310992e2a049))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.58 ([7027767](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/70277677b721ee951d868b6956c827395f2a5e0b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.59 ([84da203](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/84da2035d413036da4dbac59e7753b834825a00a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.60 ([bc52af0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bc52af0f8c735350be14c238e94134db1d744305))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.61 ([cf4420c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cf4420c7358369fedba0edc61c8e49a25177a2f7))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.62 ([1cb8d3c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1cb8d3c2a8cc4505f95b771494c68ea47276f446))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.63 ([fe148cc](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fe148ccc6af1a397c0d105214262d50ed28d617e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.64 ([c55884b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c55884bdc5c4c26c4d4b55d4e757f73a1c003fcb))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.65 ([5f76ca6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5f76ca6bf4db932c91e025c468fa7cf82dbe0ae9))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.66 ([e9205b8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e9205b810b1768c3a9be66b7f87268ff1d2edae5))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.67 ([2793283](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/279328372178f0444e4bb2303734f45daae211eb))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.68 ([5b8eafc](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5b8eafcf9b6fdd43de0aa80f9ea187eeb2c5e9b4))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.69 ([5f912df](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5f912dfe1c842580ecb32a57c3ef33c35477a8fd))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.70 ([8434e49](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8434e49952cf5c5f1a8514b171c0af84c723ee2d))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.71 ([2a1641c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2a1641c4633e32dfaa8fa3bf2efc03bc7706a5df))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.72 ([dfee3aa](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/dfee3aaf8fb1dc8cf5bc5334eaa78ade6dc7ea74))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.73 ([da43891](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/da43891b5808766db7e9739ec9d44f2125c0b6d5))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.74 ([6425637](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/64256376efe673f94d08d57170d3ec662bdeb35d))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.75 ([a23ac4c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a23ac4c4a63b51f87ba8339c9161d7a3761fc242))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.76 ([54a4350](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/54a4350366ec99ea1c03c16028f97ab6e7bdec74))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.77 ([11e280f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/11e280f0752dd25cdd18bfaee296488b2b00a0be))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.78 ([2fbafcd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2fbafcdae3e180b43fd0f3b431b60b143b7e5cc1))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.79 ([5f384e4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5f384e49831ebd6bb808a9f505615def06ce24c1))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.80 ([908ffa2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/908ffa2c9a32cb50a8316b274831c80cbb8a110e))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.81 ([b404680](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b404680774ae13a7ea910e031b8ec1ba25d99a25))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.82 ([6c4f6b6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6c4f6b631b64f28aa678216726b0ba07f519b18b))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.83 ([78081c3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/78081c39ab40637384f61c9a03718899d143a7e4))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.84 ([c9a7b1b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c9a7b1b34fa4f8c48b4a054f69ca0f16637c1ba8))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.85 ([087038e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/087038e54d2c0a4ebd56e1b2d9b4ac577309f92c))
* **deps:** update dependency xarray to v2023.10.0 ([2f3519c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2f3519ca55e222ec6ba8dbda12336568033d1593))
* **deps:** update dependency xarray to v2023.10.1 ([6c5ba4b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6c5ba4b557ec652d0924603c332ab0d4077d34b2))
* **deps:** update dependency xarray to v2023.11.0 ([62a2df5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/62a2df500886ea51c881c2b2d8be76a72ab6ec34))
* **deps:** update dependency xarray to v2023.12.0 ([bd97af0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bd97af0b4f4b3d3ef727d55fb904e3e2d5c1cb05))
* **deps:** update dependency xarray to v2023.5.0 ([dc696b7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/dc696b77f9c3c4ac64555879ce1f83bbcd220c1d))
* **deps:** update dependency xarray to v2023.6.0 ([43428cf](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/43428cf18d7d5a3a0d0d1f47ed0e72113b82f4a9))
* **deps:** update dependency xarray to v2023.7.0 ([2723dfc](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2723dfca75342d0ddcc1b207e65ac87eba0af473))
* **deps:** update dependency xarray to v2023.8.0 ([399b063](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/399b0639753956f44bd5c4393a2ae18c4d612bfd))
* **deps:** update dependency xarray to v2023.9.0 ([25db928](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/25db92802b45e0b13502a890d7469d8de0c02eb6))
* **deps:** update dependency xarray to v2024 ([99cd5f3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/99cd5f3530732c4dc1b4f41f3299368c191f1d64))
* **deps:** update dependency xarray to v2024.1.1 ([6727814](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/672781492400ee253ff0d5ea02dc12ecc7f14ae3))
* **deps:** update node.js to 18.17 ([af6e90b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/af6e90bcbfbf2de53faaee87fdef84e840a93f3b))
* **deps:** update node.js to 18.18 ([5f8e17f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5f8e17f97bc85cb1f06b0a50221a749d74178964))
* **deps:** update node.js to 20.10 ([21c0a8a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/21c0a8ac68efdd63b6294c35cb08ba72d9030553))
* **deps:** update node.js to 20.11 ([904e109](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/904e10968ed06699fce0f32ad8cf9a43e5749c50))
* **deps:** update node.js to 20.9 ([dc45ac1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/dc45ac1c6889250303ae43af0d0c69ab36d758d2))
* **deps:** update node.js to v20 ([b6fb42c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b6fb42c9969a260dec6cf0965324d5bca7c8f4c9))
* **deps:** update plugin com.gradle.enterprise to v3.13.2 ([10bd299](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/10bd299de7a566bd60f7d8dee09107d867d7896c))
* **deps:** update plugin com.gradle.enterprise to v3.13.3 ([a2ef3e9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a2ef3e98214b9152e41ae0aca6361ca18b5b9619))
* **deps:** update plugin com.gradle.enterprise to v3.13.4 ([9c8eca8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9c8eca87c26a1adf646980666cb869324704855b))
* **deps:** update plugin com.gradle.enterprise to v3.14 ([1802ebe](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1802ebe7013586e7c1e411233746eb3894fae509))
* **deps:** update plugin com.gradle.enterprise to v3.14.1 ([078910a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/078910af35fa6cd9376c814e55cacd9e31fd3cea))
* **deps:** update plugin com.gradle.enterprise to v3.15 ([fead052](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fead052ddf607e88da6bc26550bcc871b111705a))
* **deps:** update plugin com.gradle.enterprise to v3.15.1 ([1b4f634](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1b4f6344139f9e14be3735c07de296eb8b2f76dd))
* **deps:** update plugin com.gradle.enterprise to v3.16 ([bd94edd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bd94eddcc8966c3940a64b9304bffa2c064dfb50))
* **deps:** update plugin com.gradle.enterprise to v3.16.1 ([00228dd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/00228dd6027c76be82ddf72f2080d83085fc672b))
* **deps:** update plugin com.gradle.enterprise to v3.16.2 ([237d977](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/237d9777a8ef963003a32d4e511f5be2f3ef63c4))
* **deps:** update plugin gitsemver to v1.1.10 ([2179c2e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2179c2ed83ea64f35920984daf87e5b69e070a7f))
* **deps:** update plugin gitsemver to v1.1.11 ([9490d73](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9490d736389496f029a1c251efdfe50fe2ce62ff))
* **deps:** update plugin gitsemver to v1.1.13 ([cfa3bcd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cfa3bcd00fe70b23907718efbfca0064c5a2cc14))
* **deps:** update plugin gitsemver to v1.1.14 ([b7e6a94](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b7e6a946ae634dd994c73b8d6f6eeaaee298acae))
* **deps:** update plugin gitsemver to v1.1.15 ([2586e3c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2586e3cccc388f374d6612aa9b279ca5ffcc1681))
* **deps:** update plugin gitsemver to v2 ([9981d23](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9981d2308942099e785b10b32cc488fad612e50b))
* **deps:** update plugin gitsemver to v2.0.1 ([2a6aac3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2a6aac3f8ae1d204d48c1fd402f54a140988bd87))
* **deps:** update plugin gitsemver to v2.0.2 ([5fe6580](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5fe658098da02bd5b9f33f9c6377a36fa13a6e17))
* **deps:** update plugin gitsemver to v2.0.3 ([da7b9f1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/da7b9f1fe44f1e21d11c90b95abbac821c957d07))
* **deps:** update plugin gitsemver to v2.0.4 ([b35a491](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b35a4914c29b0ba70c3ec25e962d7ec36ec5bcb3))
* **deps:** update plugin gitsemver to v2.0.5 ([ec7d87d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ec7d87d689bf7ed66ee94181946fcfab0444aae5))
* **deps:** update plugin gitsemver to v3 ([950f217](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/950f2173b1be5da1c772e4d5bb6a72e7b9ef3b1e))
* **deps:** update plugin gitsemver to v3.1.0 ([7d87c19](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7d87c19ed976ce85c752450e8546d82f1a733923))
* **deps:** update plugin gitsemver to v3.1.1 ([144922b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/144922b63c23772562e0d19899eb3ab1cf00120f))
* **deps:** update plugin kotlin-qa to v0.42.0 ([35767d4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/35767d4cba5f451b015be7b4b955ed07975182bf))
* **deps:** update plugin kotlin-qa to v0.42.1 ([a2718ac](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a2718ac03ab436c902708b7f64ea6dff70a545d0))
* **deps:** update plugin kotlin-qa to v0.43.0 ([345d4da](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/345d4da04e3ac5177ee032cfcf0070016dedbba7))
* **deps:** update plugin kotlin-qa to v0.44.0 ([cc47d03](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cc47d03e4c95d98672dc92999187bd63e9deee02))
* **deps:** update plugin kotlin-qa to v0.45.0 ([2cd8410](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2cd84105b9e02ae88c17f43ea87494b28be31d08))
* **deps:** update plugin kotlin-qa to v0.46.0 ([d642fa9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d642fa9a46a4ae6749aef6d4fe53026b1b559a14))
* **deps:** update plugin kotlin-qa to v0.46.1 ([462edb9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/462edb940305180324c5b1cf8f315a85515c44ca))
* **deps:** update plugin kotlin-qa to v0.47.0 ([99c6ae0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/99c6ae05c1c71dd33dc97e01e5ac2dac404a8397))
* **deps:** update plugin kotlin-qa to v0.47.1 ([3ff6789](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3ff67896fe720468f0a01279c9c0eeff9565abac))
* **deps:** update plugin kotlin-qa to v0.48.0 ([a376e77](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a376e77edb62dce580ef4e56033a6a21ad34e0ef))
* **deps:** update plugin kotlin-qa to v0.49.0 ([cc73861](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cc7386128ef46533b6bde98e39dc31bfee7e7e46))
* **deps:** update plugin kotlin-qa to v0.49.1 ([7a68b3a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7a68b3a54ff8178e18b27bdb90b2c37fdfefd626))
* **deps:** update plugin kotlin-qa to v0.50.0 ([aab3e98](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/aab3e980457c206467701f55a9b7522457931834))
* **deps:** update plugin kotlin-qa to v0.51.0 ([634ea66](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/634ea6651bd01fbe737843178cd658518d759859))
* **deps:** update plugin kotlin-qa to v0.51.1 ([0b52567](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0b5256760ca8bfdd65c29e5b31e2dc189d3d76f5))
* **deps:** update plugin kotlin-qa to v0.52.0 ([07f92c5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/07f92c519206d0bb9c8bac5d64cecc95adc95b87))
* **deps:** update plugin kotlin-qa to v0.53.0 ([97be715](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/97be715c646a84762f3cfa16c585953a7a6184e4))
* **deps:** update plugin kotlin-qa to v0.54.0 ([a24c552](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a24c5523c025a9405b0e2d6c9848ebc7084a2cce))
* **deps:** update plugin kotlin-qa to v0.54.1 ([8be45c5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8be45c5f22c3bbb9459e9933031e9a83eb7d2e0c))
* **deps:** update plugin kotlin-qa to v0.55.1 ([d2e3dc9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d2e3dc9b0f168fb286b43202f20ea75a13878a30))
* **deps:** update plugin kotlin-qa to v0.55.2 ([2d16fbd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2d16fbd64c75cb7e6a6cb67ed9de706d239e447e))
* **deps:** update plugin kotlin-qa to v0.56.0 ([af45ef7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/af45ef7426e3c1ca700136acb203689db1cf2999))
* **deps:** update plugin kotlin-qa to v0.57.0 ([e990d56](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e990d56eb9a04702eb0b9adc761aa96088b4b1ff))
* **deps:** update plugin kotlin-qa to v0.57.1 ([033e0ed](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/033e0ed176fc075e63f66b7a8f3d8ace2c4c4e53))
* **deps:** update plugin kotlin-qa to v0.58.0 ([97d7e80](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/97d7e8066ed8e1a3d8ac7b72e6b0c8e1a5bcc0d3))
* **deps:** update plugin kotlin-qa to v0.59.0 ([869f788](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/869f788d89be2523515c261f73b0b5ac8568ea35))
* **deps:** update plugin kotlin-qa to v0.59.1 ([31703a8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/31703a88eb00501c70691c533ad80136197be064))
* **deps:** update plugin kotlin-qa to v0.60.0 ([94619a0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/94619a03c5c9548fe1ba1b3c9dc919c7cd968827))
* **deps:** update plugin multijvmtesting to v0.5.0 ([d0a918f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d0a918fae72da83d9bc571643cd9718b89a5a6bc))
* **deps:** update plugin multijvmtesting to v0.5.1 ([ea88f8f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ea88f8fb74d7c69e5bb956d2eeba83d4f5d54553))
* **deps:** update plugin multijvmtesting to v0.5.2 ([78f9255](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/78f925568c18360921040628fa45ec6c73ee3d54))
* **deps:** update plugin multijvmtesting to v0.5.3 ([5a99168](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5a991685faf011b0f19b5d085893ce5c227c957f))
* **deps:** update plugin multijvmtesting to v0.5.4 ([81f4ae7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/81f4ae73800f3f089ade6e8a23996331a3278d1c))
* **deps:** update plugin multijvmtesting to v0.5.5 ([d475b23](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d475b23169e5bf217c6e97ef85c8f45ffb31545a))
* **deps:** update plugin multijvmtesting to v0.5.6 ([c70be04](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c70be046a9d71cebebac7742076ecb0da781d707))
* **deps:** update plugin multijvmtesting to v0.5.7 ([da04983](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/da0498354a34daf28d6edcd6f67caf722dfbfe17))
* **deps:** update plugin multijvmtesting to v0.5.8 ([14293f6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/14293f6cf22244a103f29a2819677ff0546c27b4))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.6.0 ([5d4dd13](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5d4dd13971030546e434dd39954f8de4d2e4dcfc))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.7.0 ([3462ae2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3462ae28ae09db143d94ee3b84c59b7c354f7f52))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.8.0 ([ec1c5d5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ec1c5d578128f5812308ec5afbf1f2a8e8bd71ed))
* **deps:** update python docker tag to v3.11.4 ([401d40a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/401d40a6034a0ecb43cf632c987224024c13f79c))
* **deps:** update python docker tag to v3.11.5 ([91462e5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/91462e5aee6102340ad7a53bc67830ded0100752))
* **deps:** update python docker tag to v3.12.0 ([3afabf0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3afabf09103a78cd161a6c865daa347301ae7641))
* **deps:** update python docker tag to v3.12.1 ([cdc69c1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cdc69c192b6512b86f84a617df4918966acd339a))
* **deps:** update python docker tag to v3.12.2 ([6902e77](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6902e77c809cd2e78a6f777e892ba7594f0311bb))


### Bug Fixes

* fix the launch of the graphics experiment ([9651958](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9651958bcfdc95cbf629944731210f512d335075))


### Build and continuous integration

* **deps:** update actions/[up/down]load-artifact action to v4 ([#668](https://github.com/DanySK/alchemist-experiments-bootstrap/issues/668)) ([e141441](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e141441c040fd0728e8496af77415bbe4edc7a36))
* **deps:** update actions/cache action to v4 ([734d6ee](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/734d6eea7dbc0a9be41f936fe54f4b8364c65ac2))
* **deps:** update actions/checkout action to v3.5.3 ([8398de8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8398de8c71e9fe129eeb00b3eb9ba856fc38d62b))
* **deps:** update actions/checkout action to v3.6.0 ([0fb9b54](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0fb9b54a555fce11c0a9606fa08a3040657a5c2d))
* **deps:** update actions/checkout action to v4 ([7d232fc](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7d232fc3458ce438fdaa94d8de0499bf53bddc25))
* **deps:** update actions/checkout action to v4.1.0 ([7191901](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7191901ca2e66ece89ab3c7312ea0695ab02d424))
* **deps:** update actions/checkout action to v4.1.1 ([e578612](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e57861259751e3c381cdc388ad3ae4bcc55a7023))
* **deps:** update actions/download-artifact action to v4.1.1 ([58441a4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/58441a48414dbf6fe5eb02d5845aba2fa853f196))
* **deps:** update actions/download-artifact action to v4.1.2 ([468a700](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/468a7002c501820e7c0769e0669ef6d09882795a))
* **deps:** update actions/setup-node action to v3.7.0 ([4f3094b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4f3094bcd995fcba2289f70d41ee0a36e20625a6))
* **deps:** update actions/setup-node action to v3.8.0 ([a8f0852](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a8f08528dbbe41f5a9d5179a2e80187e36c5cc86))
* **deps:** update actions/setup-node action to v3.8.1 ([ad2951e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ad2951e373c1056eff3f7ecbbdeb9702a5382788))
* **deps:** update actions/setup-node action to v3.8.2 ([5512df3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5512df32c1cd1298545a652a5d6f10a0d4bee909))
* **deps:** update actions/setup-node action to v4 ([1ac1c22](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1ac1c229789a88b538b32b4887fb98c11b241dc4))
* **deps:** update actions/setup-node action to v4.0.1 ([ff53f47](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ff53f4791275e914e9aa395c5dfb9213943e95e9))
* **deps:** update actions/setup-node action to v4.0.2 ([b98efe7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b98efe76a2aef820eaa1a4ef7c964c19fb13a1f2))
* **deps:** update actions/setup-python action to v4.6.1 ([8810c2c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8810c2ce7e4e0d5846b7666594d0d7984fcde1a2))
* **deps:** update actions/setup-python action to v4.7.0 ([58323d3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/58323d32f044725fffc79e6d25bbf99bebe22690))
* **deps:** update actions/setup-python action to v4.7.1 ([e4bb109](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e4bb109eb0d74fc2f39bc586d89531c05e32f17f))
* **deps:** update actions/setup-python action to v4.8.0 ([d302a93](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d302a93e07dbc98174b77a542772200e025bd7c1))
* **deps:** update actions/setup-python action to v5 ([23c7548](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/23c7548d3c7fc25c7ac3709a5fef627db651c991))
* **deps:** update actions/upload-artifact action to v3.1.3 ([31d9cd5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/31d9cd57b221e416ccc3dff30f48a57dd2048488))
* **deps:** update actions/upload-artifact action to v4.1.0 ([00cf691](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/00cf691156297e13b5ea64b40e2da6faf6bbdaaa))
* **deps:** update actions/upload-artifact action to v4.2.0 ([c22ade2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c22ade2153f4bc29d600a09c781647e018a292bb))
* **deps:** update actions/upload-artifact action to v4.3.0 ([5b408be](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5b408bec09eb7290e1f2c4d1774ade128cc1b365))
* **deps:** update actions/upload-artifact action to v4.3.1 ([cff6bed](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cff6bed3bcee8b1d95962365efa27db5000d1a84))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.10 ([d846076](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d846076d24ac2f50be15db10b043c6c2a1a3d30d))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.11 ([d6ea2fd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d6ea2fd65571320c5fa3fafcccfebd81e9d99df9))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.12 ([fbe69a2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fbe69a2888206b31afa0cd3a389d85b2d3f164c9))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.13 ([2a98f7b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2a98f7bf33217da4b50fa933c0113c2e1f68735e))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.14 ([a1ea117](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a1ea11705d99d1f982e7509f2fdeedfb66f5fd30))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.15 ([07347f6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/07347f69ec9eff374da3e6f32d73aa5ba5a829b2))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.16 ([27d6c15](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/27d6c1543466cfb14f00e6f15ca2b0e293b9ad2f))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.17 ([228dac7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/228dac7aa1c1e60f1f4f85c79118b1199bd8530e))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.19 ([fa4ddaf](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fa4ddaf1862d7a866fbae9e8ec3a4e7053097c73))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.20 ([5dd34ab](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5dd34ab62db14b3733cafff7c6293459333c62cf))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.5 ([05f42f4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/05f42f47794ccb77c72aef30b44c9e267a7b2874))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.6 ([1997e05](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1997e05cb269448540c387f05f369b8938fcd913))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.7 ([00983e7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/00983e71d0df0c3ff5c19ec97817345703819f57))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.8 ([6d350ab](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6d350ab66d925c5d57be3e92d799224adc680579))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.9 ([b791675](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b7916755efc22baa88e6a39bd7d5ef82f2baae15))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.3.0 ([f7ecf8b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f7ecf8b9ba94ee0c997c3fcf78d351d521243636))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.3.1 ([87d5e18](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/87d5e181b5494d7cf4ccef8a44e080fb022e9476))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.3.2 ([4e09141](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4e091419fe9ee21135fce9fa1f854fcf69d43660))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.4.0 ([a999818](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a9998188207f33cdb0e1112df5101e7019d955ff))
* **mergify:** use the shared config ([e9bb4fe](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e9bb4fe72eefa42fe25016785438069e22907f70))


### General maintenance

* **release:** update gradle.properties .env versions to 1.2.0 [skip ci] ([a772834](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a7728345edc11cba3a469fd7ab68145bf19cc85d))

## [1.2.0](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.1.3...1.2.0) (2023-05-05)


### Features

* prefer fill_between to express error in line chart ([#479](https://github.com/DanySK/alchemist-experiments-bootstrap/issues/479)) ([43dc387](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/43dc387c6b9a07f6382d109dac3566ed9447224f))


### General maintenance

* **release:** update gradle.properties .env versions to 1.1.3 [skip ci] ([64691b2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/64691b2ecab41a7316b8ccac63d6a9db8ae9f381))


### Build and continuous integration

* apply org.gradle.toolchains.foojay-resolver-convention ([#407](https://github.com/DanySK/alchemist-experiments-bootstrap/issues/407)) ([fdf0a1d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fdf0a1d8bba8eeb95258d23d2235277394f65822))
* **deps:** update actions/checkout action to v3.5.1 ([cf0d0f5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/cf0d0f55fbe6e81fadc34869485aa0a2f255f566))
* **deps:** update actions/checkout action to v3.5.2 ([3ba88c7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3ba88c71a2cad4bd9ee3862c61157f76d689f3cf))
* **deps:** update actions/setup-python action to v4.6.0 ([ecbab42](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ecbab4273876dc0e63e8639babd35aadeef9965b))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.22 ([060d51d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/060d51d33710d6723bf2ce72f7820d20322c43fa))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.23 ([98e1edd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/98e1edde67bd47f35e38d8d737db52a9a206775b))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.24 ([ba72398](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ba72398ab44cec95c176280cdc82e59cc1f6dc39))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.25 ([7cfab9d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7cfab9d04e683d172eb29c753af8785e66f5613f))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.26 ([15afea2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/15afea22abf771a1f1cccdafb2feb54aa1067dde))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.0 ([e5a37d8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e5a37d8caed6eae4b6a1b9750ae15fc1d905a9e3))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.3 ([ecd00b7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ecd00b724905f50d5f3032246187d88e756360e6))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.2.4 ([832f27a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/832f27abbba701a51148d68703319462b8c9facf))


### Dependency updates

* **deps:** update alchemist to v25.10.0 ([f3908ef](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f3908ef737b55d61c1fd01fd926d1996ae51bc9c))
* **deps:** update alchemist to v25.11.0 ([8f91f4e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8f91f4e3bf4dc03c8c69de3f202001dd85530727))
* **deps:** update alchemist to v25.12.0 ([35283d4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/35283d4eaa911c5f3bfc71176a9eb424a6928093))
* **deps:** update alchemist to v25.13.0 ([9e0e5e3](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9e0e5e349b1046b4e550ef74e6caaea0c70a5fdb))
* **deps:** update alchemist to v25.13.1 ([92999a8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/92999a8bfb8fd711d1a7126d9922f6eab26dadfc))
* **deps:** update alchemist to v25.14.0 ([1b47a92](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1b47a92cc0ee0b11621caf876ccb9fe2d056b009))
* **deps:** update alchemist to v25.14.2 ([e087470](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e0874704503fe78687f312a4da289a629a3ab75d))
* **deps:** update alchemist to v25.14.3 ([d6e1d53](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d6e1d531eed94e062de25b41d6120d490a7eece8))
* **deps:** update alchemist to v25.14.4 ([bef5e74](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bef5e74661858c1d520692da10993a4c2bdbadac))
* **deps:** update alchemist to v25.14.5 ([dd65db2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/dd65db23072db3a283f37a0e20cc4ddf71c185e9))
* **deps:** update alchemist to v25.14.6 ([72decad](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/72decad1db4af48ddf05075720a29a1fd485ea4b))
* **deps:** update alchemist to v25.15.2 ([9acc552](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9acc5522804c0061e734c6624a17ac068bd59b04))
* **deps:** update alchemist to v25.15.3 ([e756ead](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e756eadd17d60c472c304a1d9f43b123215b9efe))
* **deps:** update alchemist to v25.15.4 ([16950dd](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/16950dd8fab38358f78945e4efd10a806efb269e))
* **deps:** update alchemist to v25.15.5 ([9c368dc](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9c368dca29fde80d4a9057ae0eb2db66159ac44e))
* **deps:** update alchemist to v25.16.0 ([39176ac](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/39176ac1d0a17fbc3e6aafa7301c4139cb45605d))
* **deps:** update alchemist to v25.16.1 ([d7ffc14](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d7ffc1419f5ebf415fba8a1973b8205fc35af465))
* **deps:** update alchemist to v25.8.0 ([207316a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/207316a8457a83a0be50786abc0326fbd2a3fb03))
* **deps:** update alchemist to v25.9.0 ([f141b57](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f141b57a4f4983c7e22422cd7397ea67445a7fcf))
* **deps:** update alchemist to v25.9.1 ([bd5f61a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bd5f61a5a2fb549e487ad5337e7cbffc5324e9b4))
* **deps:** update alchemist to v25.9.2 ([ec6c71c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ec6c71c00134dbf4c35e1518ea250d40eb8ea201))
* **deps:** update alchemist to v25.9.3 ([ec1e1ee](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ec1e1ee09a4b2236a91a158f473957d9891aef9f))
* **deps:** update alpine docker tag to v3.17.2 ([1112807](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/1112807129433d69997588767cd22e3bd7f21ddd))
* **deps:** update alpine docker tag to v3.17.3 ([8a0af30](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8a0af30aeea498306cc7c9f15f1e4300f4522815))
* **deps:** update dependency gradle to v8 ([8cbddea](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8cbddea867aa5d63e4107783e96e18ed87008c65))
* **deps:** update dependency gradle to v8.0.2 ([e6f90eb](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e6f90eb54aacfadb99e128bf6fe8afadf81f1b16))
* **deps:** update dependency gradle to v8.1 ([b49d8d5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b49d8d5dc5c16403b6e8d30e7800e0e840b26225))
* **deps:** update dependency gradle to v8.1.1 ([57af727](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/57af7275a8c6c305f8945102847660ef20880253))
* **deps:** update dependency matplotlib to v3.7.0 ([fc71450](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fc7145080c8aa6eba29c22ffaaf937c4070dc64e))
* **deps:** update dependency matplotlib to v3.7.1 ([58d8bc6](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/58d8bc6b6bea9d85f6ba14f91f69a78a9fb754b9))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.8.10 ([4ee4c7c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4ee4c7c59790d05a9bc213fbfa17f2a8378ebc7d))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.8.20 ([6a8a5e5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6a8a5e510a1b74400b8c6de6b46bcf49c4b80ed1))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.8.21 ([b9268b5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b9268b5fe6bb7161c7a61dc3165798fcb0843b1a))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.23 ([9749694](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9749694abd96e7a6a882e6026466f9bd84f569b4))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.24 ([fc417e2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fc417e2ebc41fa531a7fa251d0c12261e49fb885))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.25 ([300065a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/300065af5c22bdabfc469141713f33ddc412b5d8))
* **deps:** update dependency semantic-release-preconfigured-conventional-commits to v1.1.26 ([9a6248c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/9a6248c3bc08e719a86f3c9f5a18b0494ae3c008))
* **deps:** update dependency xarray to v2023.2.0 ([64febd8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/64febd82eac86f365dca083e9dfabf88cab7ddce))
* **deps:** update dependency xarray to v2023.3.0 ([5866720](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/58667209784d5bdb06858710522cf16f07eeaa67))
* **deps:** update dependency xarray to v2023.4.0 ([bfe7dcb](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/bfe7dcb7a58c7e344909a2ce84c59995b0f0fbbd))
* **deps:** update dependency xarray to v2023.4.1 ([ba80193](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ba8019369cbea2f1693582a3699dcb1db3c54b29))
* **deps:** update dependency xarray to v2023.4.2 ([704c912](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/704c9128c79d280db37a2b51a352b5fd874306c5))
* **deps:** update node.js to 18.14 ([3658e0f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3658e0fccbc4b9231481e1882381d88a85b98e5d))
* **deps:** update node.js to 18.15 ([262c0af](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/262c0af7f7f89e39c149c8a2d077724fb4281db6))
* **deps:** update node.js to 18.16 ([2222cbe](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/2222cbee7cb3fa0c1c5b10b8a3b65a30fd910a97))
* **deps:** update plugin com.gradle.enterprise to v3.12.3 ([6ccf8c9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6ccf8c919a226b280560b9b74d4f306765a9cc09))
* **deps:** update plugin com.gradle.enterprise to v3.12.4 ([126b903](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/126b90374651296f67669222df0ca755612abea9))
* **deps:** update plugin com.gradle.enterprise to v3.12.6 ([8b30cc1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8b30cc118900e8cfa7a5f7eb2c8a6773b241e429))
* **deps:** update plugin com.gradle.enterprise to v3.13 ([7464c3c](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7464c3c60e88d6687858470dfe8134c6e471fd0b))
* **deps:** update plugin com.gradle.enterprise to v3.13.1 ([a947cd5](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a947cd5e5b18b15971d8d6280d072aadd9c5d6f6))
* **deps:** update plugin gitsemver to v1.0.2 ([6582785](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/65827853038abc5a4eba6dcd8fe2427dfe99d68b))
* **deps:** update plugin gitsemver to v1.1.1 ([6a1da20](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6a1da20a52d2a05de3c30f46e845c3e1cc77fbdf))
* **deps:** update plugin gitsemver to v1.1.2 ([b77f3a9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b77f3a9fd6cd3131af7d890f7dc5e96e2522db1a))
* **deps:** update plugin gitsemver to v1.1.3 ([c8aa3ab](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c8aa3abcf7d36db096c4bc39ad058803f1809022))
* **deps:** update plugin gitsemver to v1.1.4 ([e62f9a8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e62f9a8d406c2253b8841c1f8b19f7eb51834151))
* **deps:** update plugin gitsemver to v1.1.6 ([126bebe](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/126bebe1fcd28441d0d610094523d07368ff47c6))
* **deps:** update plugin gitsemver to v1.1.7 ([7c69407](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7c694070bbba370e523cdec8a7ed8cf1f075e640))
* **deps:** update plugin gitsemver to v1.1.8 ([c64aec7](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c64aec766f1865e51a499bcebdea3b793f578d89))
* **deps:** update plugin gitsemver to v1.1.9 ([e9905da](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e9905dae7f3e334a00879243985ad2009a95faa4))
* **deps:** update plugin kotlin-qa to v0.34.0 ([c02e443](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c02e4434498ee8bc103bc88107d698f66c82af74))
* **deps:** update plugin kotlin-qa to v0.34.1 ([63d0e84](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/63d0e84fdcbc6a1d8ca2c7083811e7149a8a8f69))
* **deps:** update plugin kotlin-qa to v0.34.2 ([b06035e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/b06035efcc8f8ec7e86f1430e2bc893ba586d8c1))
* **deps:** update plugin kotlin-qa to v0.35.0 ([41031a1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/41031a1985ab9f3333fb4d981822663d641bc8e7))
* **deps:** update plugin kotlin-qa to v0.36.1 ([f4ff837](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f4ff837a0e5b5ef3321d69f1373847783e551ebe))
* **deps:** update plugin kotlin-qa to v0.38.1 ([a290e6f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a290e6f03d496dd90521707a49cdc6e24136e777))
* **deps:** update plugin kotlin-qa to v0.38.2 ([fd1cb22](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/fd1cb2281291979529741a06139dc052fcffb8b2))
* **deps:** update plugin kotlin-qa to v0.39.0 ([db65d17](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/db65d17ee17afb3834436a77b625e19b8359ffbe))
* **deps:** update plugin kotlin-qa to v0.40.0 ([7b9b396](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7b9b396b2dd96e9633f88fb3f5f25e02e6e212f8))
* **deps:** update plugin kotlin-qa to v0.41.0 ([ed52452](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ed52452b45d6d212dda1a1878a68249d76c57208))
* **deps:** update plugin multijvmtesting to v0.4.16 ([81f839d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/81f839d5baf9239784a0b7940e4551aa0ac2af61))
* **deps:** update plugin multijvmtesting to v0.4.17 ([39206e0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/39206e0ae87e9898718efb2d60cbeb420ba68f45))
* **deps:** update plugin multijvmtesting to v0.4.19 ([5e9eb9f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/5e9eb9fd51d3461d3e2826a937c309abeb4df8b4))
* **deps:** update plugin multijvmtesting to v0.4.20 ([62fd0f9](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/62fd0f961261880b7501d5896044a503fddf252a))
* **deps:** update plugin multijvmtesting to v0.4.21 ([87fe715](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/87fe7159ed4194e5f3a04b7c09d9c3a62506c3ea))
* **deps:** update plugin multijvmtesting to v0.4.22 ([7f1a26e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/7f1a26e20b0b4d152e04ad664169296ca80bdecb))
* **deps:** update plugin multijvmtesting to v0.4.23 ([4bf5b18](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4bf5b18293198fddfdbdce66dd580781315e9c23))
* **deps:** update plugin org.gradle.toolchains.foojay-resolver-convention to v0.5.0 ([de5d2bb](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/de5d2bbe901c34505aae01292b0143ebea4b883e))
* **deps:** update python docker tag to v3.11.2 ([3317d68](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/3317d68d728bbc45ab13670806ea629c81095079))
* **deps:** update python docker tag to v3.11.3 ([a6d8861](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a6d886122cab5bd922b912fd9612ee6996f60f47))

## [1.1.3](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.1.2...1.1.3) (2023-01-29)


### Bug Fixes

* **release:** move pushes with refreshed versions to the publish phase ([c185161](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/c1851619d8e302165c6eaeaf66ae52c561e1a54c))


### Documentation

* **readme:** add a way to re-run the charts generation without re-running experiments ([56c8965](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/56c8965fa8c8f9cff91e99455056392386e37440))
* **readme:** prepare a readme stub ([e7d7432](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/e7d743218d65a27dad7c463ca2b0c2f83d07ecc0))


### Dependency updates

* **deps:** update python docker tag to v3.11.1 ([77f15c1](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/77f15c137c30bd23c948c17e32ec708ce7d88e3c))


### Build and continuous integration

* always rebuild the container images ([6a1037a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6a1037a5a902e85093f4c2d8a22c7adde31bce53))
* validate the Gradle wrapper on Linux only ([8846942](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8846942331bc06bec28d440b42be31054bf07a33))

## [1.1.2](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.1.1...1.1.2) (2023-01-24)


### Bug Fixes

* **release:** add a preparatory commit for the version updates ([f811f3d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f811f3d876b776baf6529dddd36f37cada4236b9))
* **release:** push the updated files after version calculation ([0311e56](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0311e56a5110d883c2c71a8a7002445fdbf9adf6))


### General maintenance

* **release:** update version descriptors to 1.1.2 ([298c888](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/298c88848084eb3b9af658e867d736bec4e01496))


### Build and continuous integration

* **release:** skip the CI process for release commits ([8a0732f](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/8a0732f82b17f5dc85382c4de2716f4d6a10f486))

## [1.1.2](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.1.1...1.1.2) (2023-01-24)


### Bug Fixes

* **release:** add a preparatory commit for the version updates ([f811f3d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/f811f3d876b776baf6529dddd36f37cada4236b9))
* **release:** push the updated files after version calculation ([0311e56](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/0311e56a5110d883c2c71a8a7002445fdbf9adf6))

## [1.1.1](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.1.0...1.1.1) (2023-01-24)


### Bug Fixes

* **release:** move the preparation commands to the prepare phase ([ee52de2](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ee52de20fa26653febcfdc158884b38ad2a209d8))

## [1.1.0](https://github.com/DanySK/alchemist-experiments-bootstrap/compare/1.0.1...1.1.0) (2023-01-24)


### Features

* run simulations with more variables to make decent charts ([77e6d6d](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/77e6d6d64b2ce74992c2c9cd35b75a2860571a50))


### Bug Fixes

* **build:** remove deprecated variable assignment ([6099baf](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/6099baf6f9e666e066f8fd7623a6198521eb46b4))
* **build:** remove generated data after the simulation container build ([a79dab4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a79dab48e41dfc09b213afcae7e29f9767fb9079))
* **build:** switch to modern JSON effects ([a0ede3b](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a0ede3bb2bfa5a868d3d918e2b59d2edd95dd39c))
* **ci:** read the docker password from the CI secrets ([689a3a4](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/689a3a40fef2e65a9dc6eaab3a07378af955b510))
* **ci:** use a separate concurrency group for the container check job ([d06f389](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d06f3894edb14f67693aa8da043f670cdbb4a2b3))
* **release:** publish the images built in CI ([4c7d849](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/4c7d8495adfac26818aa87cab08cc25f954d59aa))


### Dependency updates

* **deps:** update alchemist to v25.7.2 ([00b615a](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/00b615ae14b62f677b7410886fef189a61c9645c))
* **deps:** update dependency xarray to v2023 ([32cc855](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/32cc85583d6967e1d2e740a9641c5011997bb979))


### Build and continuous integration

* add a docker check job ([ca6ac93](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/ca6ac934f5e3aeb63eb3350a2d4bdc22ea7cb056))
* prepare a containerized version of the experiment ([d0ff60e](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d0ff60eec241b67a43064796fdc24f930d698394))


### General maintenance

* **build:** remove aggressive heap settings ([a40d0be](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/a40d0be30b95ec93b5e8baaa32961211d5d6c706))
* delete Eclipse settings ([807f8d0](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/807f8d0835162d4bf96baf81b4dd686c60abbd67))
* ignore idea, spyder, gradle, and charts folder ([d92b6e8](https://github.com/DanySK/alchemist-experiments-bootstrap/commit/d92b6e8d52c9cfe0d83de9dc5a03cf26e93d18e6))

## [1.0.1](https://github.com/DanySK/Alchemist-experiments-startup/compare/1.0.0...1.0.1) (2023-01-19)


### Documentation

* clarify the need for the DEPLOYMENT_TOKEN in the readme ([534533b](https://github.com/DanySK/Alchemist-experiments-startup/commit/534533b7826dce6ebf3304fdea2807aa1c9d982b))


### Build and continuous integration

* cancel in-progress charts rendering on new pushes ([a377004](https://github.com/DanySK/Alchemist-experiments-startup/commit/a3770040cdc89b8a3805961d5774f8bddeb2c7b7))
* cancel in-progress simulation checks on new pushes ([0e37030](https://github.com/DanySK/Alchemist-experiments-startup/commit/0e37030dae0c91f615b5fa2c3bedf2d18aca2194))
* **deps:** update dependency macos github actions runner to v12 ([e219ab1](https://github.com/DanySK/Alchemist-experiments-startup/commit/e219ab16b0ceb4c8ca75795660c5d3b4fba9a3f9))
* **deps:** update dependency windows github actions runner to v22 ([238a30d](https://github.com/DanySK/Alchemist-experiments-startup/commit/238a30dda649405d7a5e3fd8729d8182df499d4d))
* limit the concurrency of the release jobs ([6b3c238](https://github.com/DanySK/Alchemist-experiments-startup/commit/6b3c238de08c2f9b9501c21f75ecb2001f0294a8))
* recover the build functionality ([6197c5c](https://github.com/DanySK/Alchemist-experiments-startup/commit/6197c5cc5ecd23272d7dbe82765a3a5b8c06d419))


### Dependency updates

* **deps:** update alchemist to v25.7.1 ([b54e7c5](https://github.com/DanySK/Alchemist-experiments-startup/commit/b54e7c5e7930c35772d55ebb19c2c163f5e85aec))
* **deps:** update plugin com.gradle.enterprise to v3.12.2 ([4513d0f](https://github.com/DanySK/Alchemist-experiments-startup/commit/4513d0feb288272453a4ff1b9643bfa802f907ac))
* **deps:** update plugin gitsemver to v1 ([87b688e](https://github.com/DanySK/Alchemist-experiments-startup/commit/87b688ee5c2fe3072f8f3107686d25aa6f6749a2))
* **deps:** update plugin tasktree to v2.1.1 ([761aded](https://github.com/DanySK/Alchemist-experiments-startup/commit/761aded54c3f9da7f35e1a035920b859d79d6bbf))
* **deps:** update python docker tag to v3.11.1 ([920a338](https://github.com/DanySK/Alchemist-experiments-startup/commit/920a338227325a047a8d5ab309e6f92390168e1a))

## 1.0.0 (2023-01-19)


### Bug Fixes

* **charting:** convert Java's 'Infinity' to a Python-friendly 1e30000 ([f432fae](https://github.com/DanySK/Alchemist-experiments-startup/commit/f432fae470f7bc6ade3c572d3e794acc620059c3))
* **deps:** update alchemist to v24.1.2 ([a39e289](https://github.com/DanySK/Alchemist-experiments-startup/commit/a39e28918a9bfdcf2bdbc5c95c4def2ca9baf7a7))


### General maintenance

* delete unused scripts folder ([d20f7c5](https://github.com/DanySK/Alchemist-experiments-startup/commit/d20f7c56a30bd5e6e8e8faa8b00542ce128b616e))
* delete unused version.properties ([068028c](https://github.com/DanySK/Alchemist-experiments-startup/commit/068028c2e3679ce47a100bdbc1750509e8da3a3a))


### Dependency updates

* **deps:** update alchemist to v18 ([7620fbd](https://github.com/DanySK/Alchemist-experiments-startup/commit/7620fbd05268f2b0bc8e678e017ab86b90c55389))
* **deps:** update alchemist to v19 ([8a6073f](https://github.com/DanySK/Alchemist-experiments-startup/commit/8a6073f51376617aaf2b5ff2547ec31125048e2e))
* **deps:** update alchemist to v19.0.1 ([34d2fbe](https://github.com/DanySK/Alchemist-experiments-startup/commit/34d2fbe1af969fe05204f1be5a4859764c8534d7))
* **deps:** update alchemist to v19.0.2 ([cefb051](https://github.com/DanySK/Alchemist-experiments-startup/commit/cefb0510c26df3ec20a63f5c368adcc5abc67876))
* **deps:** update alchemist to v19.0.3 ([88da774](https://github.com/DanySK/Alchemist-experiments-startup/commit/88da7743c4dc58ecb471a245ccf75d030b159ae2))
* **deps:** update alchemist to v19.0.4 ([e7a2544](https://github.com/DanySK/Alchemist-experiments-startup/commit/e7a2544dcf6459594ff64cae09dce511776f907e))
* **deps:** update alchemist to v19.1.0 ([5614547](https://github.com/DanySK/Alchemist-experiments-startup/commit/56145479ccd56fcec4f72e3852ae5edcaa8e7c13))
* **deps:** update alchemist to v19.1.1 ([9fa0a33](https://github.com/DanySK/Alchemist-experiments-startup/commit/9fa0a339b787a927e3c0fcd48e86a47fb690f578))
* **deps:** update alchemist to v19.2.0 ([8bf0669](https://github.com/DanySK/Alchemist-experiments-startup/commit/8bf0669c08db14e75072605faa09de4596e78168))
* **deps:** update alchemist to v20 ([aa28f14](https://github.com/DanySK/Alchemist-experiments-startup/commit/aa28f146f6320da547e8de526d498190ef3e2e51))
* **deps:** update alchemist to v20.0.1 ([4d2ee2c](https://github.com/DanySK/Alchemist-experiments-startup/commit/4d2ee2cc3e16c08edae585cfda0cef831b4b631d))
* **deps:** update alchemist to v21 ([f2e52c2](https://github.com/DanySK/Alchemist-experiments-startup/commit/f2e52c258b29acebc339189fbef720c64b09eaf7))
* **deps:** update alchemist to v21.0.1 ([a46aaae](https://github.com/DanySK/Alchemist-experiments-startup/commit/a46aaae1d7c6fbbcea1e547440c7a50c4c6cf71e))
* **deps:** update alchemist to v21.0.8 ([7ab2a39](https://github.com/DanySK/Alchemist-experiments-startup/commit/7ab2a397b1216267e3d3552cae91f9b6be8b1a8a))
* **deps:** update alchemist to v22 ([ed65e60](https://github.com/DanySK/Alchemist-experiments-startup/commit/ed65e607777043cc457b4508e6e62434e09b327d))
* **deps:** update alchemist to v23 ([2c10f27](https://github.com/DanySK/Alchemist-experiments-startup/commit/2c10f2730bbeb827344d16943f56ea1a83175e44))
* **deps:** update alchemist to v24 ([2114e88](https://github.com/DanySK/Alchemist-experiments-startup/commit/2114e886b9f6621ec9516a674fd27f15b6553a1a))
* **deps:** update alchemist to v24.0.3 ([85abe2e](https://github.com/DanySK/Alchemist-experiments-startup/commit/85abe2eb86ccdd205b14059f7a9b5044a2116c63))
* **deps:** update alchemist to v24.0.4 ([3ecee08](https://github.com/DanySK/Alchemist-experiments-startup/commit/3ecee08b71f5e12864de0b50a37d4152887a7dcf))
* **deps:** update alchemist to v24.0.5 ([6ba51e2](https://github.com/DanySK/Alchemist-experiments-startup/commit/6ba51e2b9045b3e58e92b2b022764f2f3f67884b))
* **deps:** update alchemist to v24.0.7 ([71c2035](https://github.com/DanySK/Alchemist-experiments-startup/commit/71c2035ad3d302ec225911de30defe42e41cfefa))
* **deps:** update alchemist to v24.0.8 ([2bdf0d2](https://github.com/DanySK/Alchemist-experiments-startup/commit/2bdf0d2637b61ac8c7948561ff65da17df75bfd3))
* **deps:** update alchemist to v24.1.0 ([ee1726b](https://github.com/DanySK/Alchemist-experiments-startup/commit/ee1726bfd66e8031ba0a23b0f957445c112c849b))
* **deps:** update alchemist to v24.1.1 ([5d7702e](https://github.com/DanySK/Alchemist-experiments-startup/commit/5d7702e6e2aa4bb445954407a5f8c2b37ddb039f))
* **deps:** update alchemist to v24.1.10 ([62b199d](https://github.com/DanySK/Alchemist-experiments-startup/commit/62b199da2af78bf2cb75bce8f1e6cc539ca17f15))
* **deps:** update alchemist to v24.1.11 ([96c5277](https://github.com/DanySK/Alchemist-experiments-startup/commit/96c5277a8b080ae5b8c887b9410eeb4771610095))
* **deps:** update alchemist to v24.1.12 ([ac4e62e](https://github.com/DanySK/Alchemist-experiments-startup/commit/ac4e62e1988bb220f63411834ef330f6699ca01b))
* **deps:** update alchemist to v24.1.13 ([f5c0199](https://github.com/DanySK/Alchemist-experiments-startup/commit/f5c0199016bf02ce482fcf20596256758fac0140))
* **deps:** update alchemist to v24.1.14 ([fc92d67](https://github.com/DanySK/Alchemist-experiments-startup/commit/fc92d6708f8bc8e628f044af59dace2fb6995d09))
* **deps:** update alchemist to v24.1.15 ([16c3926](https://github.com/DanySK/Alchemist-experiments-startup/commit/16c3926759d394155e16c1028f77108199268feb))
* **deps:** update alchemist to v24.1.16 ([a46b725](https://github.com/DanySK/Alchemist-experiments-startup/commit/a46b7259e90967517ae59b939b0e89ba5beecfb1))
* **deps:** update alchemist to v24.1.3 ([c568d69](https://github.com/DanySK/Alchemist-experiments-startup/commit/c568d694057cfe2ea910b8c8c4cf96e2a51aa3a7))
* **deps:** update alchemist to v24.1.4 ([b8e0ccd](https://github.com/DanySK/Alchemist-experiments-startup/commit/b8e0ccdb0b9fee66855aeb70cdc73e4cee4b2571))
* **deps:** update alchemist to v24.1.5 ([7878a29](https://github.com/DanySK/Alchemist-experiments-startup/commit/7878a299014d19b27616a63d14a81538a74d5a61))
* **deps:** update alchemist to v24.1.6 ([d8a385c](https://github.com/DanySK/Alchemist-experiments-startup/commit/d8a385cd5a214dd7439163999a338e2c96e84e65))
* **deps:** update alchemist to v24.1.7 ([37f4d79](https://github.com/DanySK/Alchemist-experiments-startup/commit/37f4d79a245970988e15fc6deda95102638e75fe))
* **deps:** update alchemist to v24.1.9 ([f7984a9](https://github.com/DanySK/Alchemist-experiments-startup/commit/f7984a960d3bbf5906d10474cffe4dac0657d673))
* **deps:** update alchemist to v25 ([7db2f48](https://github.com/DanySK/Alchemist-experiments-startup/commit/7db2f48b4f4842511221efeb9eeab977e49f8294))
* **deps:** update alchemist to v25.2.0 ([880b5b9](https://github.com/DanySK/Alchemist-experiments-startup/commit/880b5b9aac081194bddf469a27cf480a99898285))
* **deps:** update alchemist to v25.2.1 ([5b7309e](https://github.com/DanySK/Alchemist-experiments-startup/commit/5b7309e3beb4c4544d61597ef68df2748572f32a))
* **deps:** update alchemist to v25.3.0 ([2d6fab5](https://github.com/DanySK/Alchemist-experiments-startup/commit/2d6fab591f2f55f447650a9d49dae2e3a8f362f1))
* **deps:** update alchemist to v25.4.0 ([6ac914a](https://github.com/DanySK/Alchemist-experiments-startup/commit/6ac914a735e1ed0edb06f3e957ccba54dd99593b))
* **deps:** update alchemist to v25.4.1 ([0e9be1f](https://github.com/DanySK/Alchemist-experiments-startup/commit/0e9be1fbe96420e43f844d8c7ebab6a44ac488aa))
* **deps:** update alchemist to v25.4.2 ([fe0b221](https://github.com/DanySK/Alchemist-experiments-startup/commit/fe0b2211a9ded5b05baf3a7791731fa9c4a1cbf1))
* **deps:** update alchemist to v25.5.0 ([71da78f](https://github.com/DanySK/Alchemist-experiments-startup/commit/71da78fb38d07a46c2b72939507cebf4295e5ce9))
* **deps:** update alchemist to v25.6.0 ([7ec8059](https://github.com/DanySK/Alchemist-experiments-startup/commit/7ec805978ff925f3622007e26870c3b08f2fd603))
* **deps:** update alchemist to v25.7.0 ([6cdf812](https://github.com/DanySK/Alchemist-experiments-startup/commit/6cdf812d480927c85447f260a2809d5dc8c71703))
* **deps:** update dependency gradle to v7.3 ([f3627dd](https://github.com/DanySK/Alchemist-experiments-startup/commit/f3627ddb0809bfb9fc12e8e6de993ebaccdd704d))
* **deps:** update dependency gradle to v7.3.1 ([0fd0ada](https://github.com/DanySK/Alchemist-experiments-startup/commit/0fd0ada3dec2c76b4380448ea08b63488bf1c2ff))
* **deps:** update dependency gradle to v7.3.2 ([0858784](https://github.com/DanySK/Alchemist-experiments-startup/commit/0858784f9558fb8ad18524ed6712245bd0b10037))
* **deps:** update dependency gradle to v7.3.3 ([702a7ea](https://github.com/DanySK/Alchemist-experiments-startup/commit/702a7ea31643bb1c1e044dfb64f8e59ff6f64e1e))
* **deps:** update dependency gradle to v7.4 ([f7b2f02](https://github.com/DanySK/Alchemist-experiments-startup/commit/f7b2f02856ae0dd30b86df4920ef3bb90b866d32))
* **deps:** update dependency gradle to v7.4.1 ([77907fb](https://github.com/DanySK/Alchemist-experiments-startup/commit/77907fbc092c97e7144902c6edf70adf49f8287b))
* **deps:** update dependency gradle to v7.4.2 ([219e503](https://github.com/DanySK/Alchemist-experiments-startup/commit/219e50312aaee11b4c73f38d7bbd190e7ef6177c))
* **deps:** update dependency gradle to v7.5 ([e4f1202](https://github.com/DanySK/Alchemist-experiments-startup/commit/e4f1202216a80c263a810e22a0f815a795397826))
* **deps:** update dependency gradle to v7.5.1 ([75a2c8c](https://github.com/DanySK/Alchemist-experiments-startup/commit/75a2c8ca4ebde5e4115d3672d5a6ba502358ecda))
* **deps:** update dependency gradle to v7.6 ([cf5df22](https://github.com/DanySK/Alchemist-experiments-startup/commit/cf5df22f1501a3155e121d5e60ea97a25c791229))
* **deps:** update dependency it.unibo.alchemist:alchemist to v12.0.3 ([a2cfa21](https://github.com/DanySK/Alchemist-experiments-startup/commit/a2cfa2148b05bcebd1dc5d0fa39bada6a69dcc8b))
* **deps:** update dependency it.unibo.alchemist:alchemist to v13.0.3 ([7633167](https://github.com/DanySK/Alchemist-experiments-startup/commit/7633167bb89c1e9ebda2c6287c5774a261f39a40))
* **deps:** update dependency it.unibo.alchemist:alchemist to v13.0.6 ([f2f19e4](https://github.com/DanySK/Alchemist-experiments-startup/commit/f2f19e4cebbefabfcfb4440baf1adc47c7f65ad1))
* **deps:** update dependency it.unibo.alchemist:alchemist-incarnation-protelis to v12.0.4 ([fbd0a74](https://github.com/DanySK/Alchemist-experiments-startup/commit/fbd0a74a566dd47c981baf5df7bdb43b10f9a487))
* **deps:** update dependency it.unibo.alchemist:alchemist-incarnation-scafi to v12.1.7 ([f6e9704](https://github.com/DanySK/Alchemist-experiments-startup/commit/f6e9704bc27ef3b6de2a946cc031b35bdff4cf24))
* **deps:** update dependency it.unibo.alchemist:alchemist-incarnation-scafi to v13.0.4 ([7a36e21](https://github.com/DanySK/Alchemist-experiments-startup/commit/7a36e21c2968853b418d7cfa9132f897b99ba54a))
* **deps:** update dependency matplotlib to v3.5.0 ([6fedce4](https://github.com/DanySK/Alchemist-experiments-startup/commit/6fedce4e0a9b8f5d46897d53d4b4c92e3e3164af))
* **deps:** update dependency matplotlib to v3.5.1 ([005ec60](https://github.com/DanySK/Alchemist-experiments-startup/commit/005ec60a73d66ccb9f5521562294011e2ee811f6))
* **deps:** update dependency matplotlib to v3.5.2 ([b8fa622](https://github.com/DanySK/Alchemist-experiments-startup/commit/b8fa62294ca02f4cac35b9802018924715cad146))
* **deps:** update dependency matplotlib to v3.5.3 ([2937750](https://github.com/DanySK/Alchemist-experiments-startup/commit/293775015498cf425084d6019a967ae22712c1c5))
* **deps:** update dependency matplotlib to v3.6.0 ([8b261a2](https://github.com/DanySK/Alchemist-experiments-startup/commit/8b261a253460df5e0106fb8a84ca49f264781504))
* **deps:** update dependency matplotlib to v3.6.1 ([bb6219d](https://github.com/DanySK/Alchemist-experiments-startup/commit/bb6219d80b1303812da26d84cd7396728a6c3aae))
* **deps:** update dependency matplotlib to v3.6.2 ([2c3cb99](https://github.com/DanySK/Alchemist-experiments-startup/commit/2c3cb994f870559041935997030ece2cee4a3afa))
* **deps:** update dependency matplotlib to v3.6.3 ([8c446fd](https://github.com/DanySK/Alchemist-experiments-startup/commit/8c446fd048cd6a1a4258b78d270be14242e704dd))
* **deps:** update dependency openjdk to v18 ([43e2783](https://github.com/DanySK/Alchemist-experiments-startup/commit/43e278310b5797e8c6ee4fdeb54e1978e61524b4))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.7.0 ([79f1b47](https://github.com/DanySK/Alchemist-experiments-startup/commit/79f1b47ba31cda8db54ab11b0b0ef5c416d36c3e))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.7.10 ([e9e4155](https://github.com/DanySK/Alchemist-experiments-startup/commit/e9e4155eb1fcad2557a746381d9015a451ff9530))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.7.20 ([5437b3e](https://github.com/DanySK/Alchemist-experiments-startup/commit/5437b3e30d0ceb34ff9b437aa0a2d64d671d68ea))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.7.21 ([7c64e39](https://github.com/DanySK/Alchemist-experiments-startup/commit/7c64e395255d21a5c5902263f0a34beefe957404))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.7.22 ([bbeeb01](https://github.com/DanySK/Alchemist-experiments-startup/commit/bbeeb0138c169147f8818d76fb9c41e05254ff33))
* **deps:** update dependency org.jetbrains.kotlin.jvm to v1.8.0 ([95a34dd](https://github.com/DanySK/Alchemist-experiments-startup/commit/95a34dd8180aa2a689cc4256a9f2628014370ba2))
* **deps:** update dependency python to v3.10.4 ([f4d6713](https://github.com/DanySK/Alchemist-experiments-startup/commit/f4d67134b9d1f38869d8d4d6430217188739c223))
* **deps:** update dependency xarray to v0.20.2 ([17f722d](https://github.com/DanySK/Alchemist-experiments-startup/commit/17f722df695d8912f6432e0767b7fe73a790890b))
* **deps:** update dependency xarray to v0.21.0 ([255c118](https://github.com/DanySK/Alchemist-experiments-startup/commit/255c118b8d1cec68c36899ea5d7b81d585384274))
* **deps:** update dependency xarray to v0.21.1 ([62f342d](https://github.com/DanySK/Alchemist-experiments-startup/commit/62f342d5ad872c2783f9ca1357a925ec668acf2a))
* **deps:** update dependency xarray to v2022 ([29e742b](https://github.com/DanySK/Alchemist-experiments-startup/commit/29e742b0a246048c584a130bab2b81ece70c448a))
* **deps:** update dependency xarray to v2022.10.0 ([bc3ef08](https://github.com/DanySK/Alchemist-experiments-startup/commit/bc3ef08bf8895dffd04f4b1ae8eda8f9546fdf13))
* **deps:** update dependency xarray to v2022.11.0 ([45c4b38](https://github.com/DanySK/Alchemist-experiments-startup/commit/45c4b389d46f5f0904aacef519972fa7cf94cd9e))
* **deps:** update dependency xarray to v2022.12.0 ([e032eab](https://github.com/DanySK/Alchemist-experiments-startup/commit/e032eabae1ea7d6b516ee9fedd34c3b4372cb825))
* **deps:** update dependency xarray to v2022.6.0 ([7d278b6](https://github.com/DanySK/Alchemist-experiments-startup/commit/7d278b6a3cff33f1262797ebc1df03b8eedf0386))
* **deps:** update dependency xarray to v2022.9.0 ([f81445d](https://github.com/DanySK/Alchemist-experiments-startup/commit/f81445d91b3136c9c68bdb8981e6d17b2b824907))
* **deps:** update it.unibo.alchemist ([ec982b1](https://github.com/DanySK/Alchemist-experiments-startup/commit/ec982b13114dbfde7ac8f50b99b0d9c42637dff3))
* **deps:** update it.unibo.alchemist to v12 ([b23827c](https://github.com/DanySK/Alchemist-experiments-startup/commit/b23827c2e3352c31e05e837477112f57939b022a))
* **deps:** update it.unibo.alchemist to v12.1.2 ([d3552b0](https://github.com/DanySK/Alchemist-experiments-startup/commit/d3552b02a26fcf3a60675ff1280ee553e6450b15))
* **deps:** update it.unibo.alchemist to v12.1.3 ([6adf430](https://github.com/DanySK/Alchemist-experiments-startup/commit/6adf43017abb5df131e35ff6ceb029ec65f74951))
* **deps:** update it.unibo.alchemist to v12.1.4 ([f9b8a53](https://github.com/DanySK/Alchemist-experiments-startup/commit/f9b8a538458c374bd858d324f7ca264f40ccfd3b))
* **deps:** update it.unibo.alchemist to v12.1.5 ([5e1b2ab](https://github.com/DanySK/Alchemist-experiments-startup/commit/5e1b2ab5a1c3b3abccaf33674097302ec60a0e0f))
* **deps:** update it.unibo.alchemist to v12.1.6 ([5bc3492](https://github.com/DanySK/Alchemist-experiments-startup/commit/5bc34926e79881e0de8b21df6fde415d27d438bb))
* **deps:** update it.unibo.alchemist to v12.2.0 ([841b7f5](https://github.com/DanySK/Alchemist-experiments-startup/commit/841b7f594061c3fc177c25c2e6743080efb599c8))
* **deps:** update it.unibo.alchemist to v12.2.1 ([58a2e7f](https://github.com/DanySK/Alchemist-experiments-startup/commit/58a2e7f3640fa5b566041cd79bd39b7d01e17cde))
* **deps:** update it.unibo.alchemist to v12.2.10 ([81d9e84](https://github.com/DanySK/Alchemist-experiments-startup/commit/81d9e84f84e4a8e3f334ad499346aaa02cc2f159))
* **deps:** update it.unibo.alchemist to v12.2.11 ([2c8228d](https://github.com/DanySK/Alchemist-experiments-startup/commit/2c8228d25518357ed27648ee71c59c979900223f))
* **deps:** update it.unibo.alchemist to v12.2.7 ([9b6fedc](https://github.com/DanySK/Alchemist-experiments-startup/commit/9b6fedc7e498d0c691d25ee31df57281f72eaeb2))
* **deps:** update it.unibo.alchemist to v12.2.8 ([c2011eb](https://github.com/DanySK/Alchemist-experiments-startup/commit/c2011eb89c391480ec5f9c54a7c6c24a5347e425))
* **deps:** update it.unibo.alchemist to v12.2.9 ([523b91e](https://github.com/DanySK/Alchemist-experiments-startup/commit/523b91ebe35055987a5e5d5546988a43c8de9d55))
* **deps:** update it.unibo.alchemist to v13 ([d378116](https://github.com/DanySK/Alchemist-experiments-startup/commit/d378116296ef7fcb4996fb5e58bfb96326333b73))
* **deps:** update it.unibo.alchemist to v13.0.1 ([9140444](https://github.com/DanySK/Alchemist-experiments-startup/commit/9140444a7be9f0fe6afb8e75b6a03ee0969e211d))
* **deps:** update it.unibo.alchemist to v13.0.2 ([53d19c6](https://github.com/DanySK/Alchemist-experiments-startup/commit/53d19c64ccbc16cf48a8518e1991b647dae4bc7b))
* **deps:** update it.unibo.alchemist to v13.0.5 ([612f656](https://github.com/DanySK/Alchemist-experiments-startup/commit/612f656d0a2f3c30b8e6b5ab414fda28df03995c))
* **deps:** update it.unibo.alchemist to v14 ([b0e5e2d](https://github.com/DanySK/Alchemist-experiments-startup/commit/b0e5e2d69687337203a045d6085203e98ba80cf3))
* **deps:** update it.unibo.alchemist to v14.0.1 ([7ddb5bc](https://github.com/DanySK/Alchemist-experiments-startup/commit/7ddb5bc2f9da615572bcbc8f5e98d59b482241b3))
* **deps:** update it.unibo.alchemist to v14.0.2 ([2514a57](https://github.com/DanySK/Alchemist-experiments-startup/commit/2514a5717385b7a125808053c270568a362496d0))
* **deps:** update it.unibo.alchemist to v14.1.0 ([26f2cf2](https://github.com/DanySK/Alchemist-experiments-startup/commit/26f2cf2f8870cd06deb059d6d361bf2b19dd1ef8))
* **deps:** update it.unibo.alchemist to v15 ([19668e9](https://github.com/DanySK/Alchemist-experiments-startup/commit/19668e96caab03bff6028033157fda5912454b30))
* **deps:** update it.unibo.alchemist to v15.0.2 ([fee8256](https://github.com/DanySK/Alchemist-experiments-startup/commit/fee825694d769f5a6abe611309f3d0eb9643c276))
* **deps:** update it.unibo.alchemist to v15.0.3 ([17fe54c](https://github.com/DanySK/Alchemist-experiments-startup/commit/17fe54cf33fa96e25060ba084ffda3c93e636793))
* **deps:** update it.unibo.alchemist to v15.0.4 ([7ac83ed](https://github.com/DanySK/Alchemist-experiments-startup/commit/7ac83ed6db6ce22537f78258a6a2f9cc9508c6d9))
* **deps:** update it.unibo.alchemist to v16 ([e89b90e](https://github.com/DanySK/Alchemist-experiments-startup/commit/e89b90e664d809bace7a295b1f4691ea0fdba630))
* **deps:** update it.unibo.alchemist to v17 ([2174d33](https://github.com/DanySK/Alchemist-experiments-startup/commit/2174d3313a78092d368864631b7edd779d02a0b3))
* **deps:** update it.unibo.alchemist to v17.0.1 ([92b76f0](https://github.com/DanySK/Alchemist-experiments-startup/commit/92b76f07582c7db224ab4674113c673a9f06f5d5))
* **deps:** update it.unibo.alchemist to v17.0.2 ([e9ed64d](https://github.com/DanySK/Alchemist-experiments-startup/commit/e9ed64d1e6b01d438db1d4c8d7754c04d7e1ca94))
* **deps:** update it.unibo.alchemist to v17.0.4 ([00b0890](https://github.com/DanySK/Alchemist-experiments-startup/commit/00b0890e14d1ba4fd43f9ecd0d4a05e32db9bde4))
* **deps:** update plugin com.gradle.enterprise to v3.10 ([ec84f24](https://github.com/DanySK/Alchemist-experiments-startup/commit/ec84f24b85438a672a8c15ed36e1fa06410ff14c))
* **deps:** update plugin com.gradle.enterprise to v3.10.1 ([dc0eb15](https://github.com/DanySK/Alchemist-experiments-startup/commit/dc0eb156b0f9e7eacd898627b17ef22442efb539))
* **deps:** update plugin com.gradle.enterprise to v3.10.2 ([540fb9e](https://github.com/DanySK/Alchemist-experiments-startup/commit/540fb9e22d52d7edf0228e1730b2d4c0d37836df))
* **deps:** update plugin com.gradle.enterprise to v3.10.3 ([93639c8](https://github.com/DanySK/Alchemist-experiments-startup/commit/93639c854cd8917efe5fca7ae8320ec064c062f1))
* **deps:** update plugin com.gradle.enterprise to v3.11 ([39303c0](https://github.com/DanySK/Alchemist-experiments-startup/commit/39303c0da12622934bc8e47ea56acc616cc764da))
* **deps:** update plugin com.gradle.enterprise to v3.11.1 ([377af6a](https://github.com/DanySK/Alchemist-experiments-startup/commit/377af6a419a3a5638b59a11824c8304364b567de))
* **deps:** update plugin com.gradle.enterprise to v3.7.2 ([9d81f38](https://github.com/DanySK/Alchemist-experiments-startup/commit/9d81f388168eaa5b1d837bccc41390d9c35af922))
* **deps:** update plugin com.gradle.enterprise to v3.8 ([c8e51a1](https://github.com/DanySK/Alchemist-experiments-startup/commit/c8e51a17c19f398df874e5bf56b63d45af0cedc0))
* **deps:** update plugin com.gradle.enterprise to v3.8.1 ([36c0696](https://github.com/DanySK/Alchemist-experiments-startup/commit/36c0696ba4bf633bb3b4eef8531795f7566c42fe))
* **deps:** update plugin com.gradle.enterprise to v3.9 ([d5709bd](https://github.com/DanySK/Alchemist-experiments-startup/commit/d5709bdd5bd23eac4ca586930d951a21f03e1f06))
* **deps:** update plugin kotlin-jvm to v1.6.0 ([f8e974e](https://github.com/DanySK/Alchemist-experiments-startup/commit/f8e974e861aef31157c3581c7fc8b59d55da3f36))
* **deps:** update plugin kotlin-jvm to v1.6.10 ([bcaf3d2](https://github.com/DanySK/Alchemist-experiments-startup/commit/bcaf3d2487aaeeb2df9e5fcd3b3f259218d2f27d))
* **deps:** update plugin kotlin-jvm to v1.6.20 ([62c8e30](https://github.com/DanySK/Alchemist-experiments-startup/commit/62c8e309d221950b6c550a5c8377e5c5db0d3bfc))
* **deps:** update plugin kotlin-jvm to v1.6.21 ([db462dc](https://github.com/DanySK/Alchemist-experiments-startup/commit/db462dcf7610cdec80014d73b19d8e6610847768))
* **deps:** update plugin kotlin-qa to v0.10.0 ([de04a9e](https://github.com/DanySK/Alchemist-experiments-startup/commit/de04a9e3e83b07eb6a6ffcc4b24abda90233f2b7))
* **deps:** update plugin kotlin-qa to v0.10.1 ([672035b](https://github.com/DanySK/Alchemist-experiments-startup/commit/672035b121e00ded00dcb72e8b6558d860269d89))
* **deps:** update plugin kotlin-qa to v0.12.0 ([555a314](https://github.com/DanySK/Alchemist-experiments-startup/commit/555a3144327f7b0171a349489afd72a7b3ca2d58))
* **deps:** update plugin kotlin-qa to v0.12.1 ([3a24bfe](https://github.com/DanySK/Alchemist-experiments-startup/commit/3a24bfe93330f90441f4fa72f5ea683001a717c3))
* **deps:** update plugin kotlin-qa to v0.13.0 ([1b700a7](https://github.com/DanySK/Alchemist-experiments-startup/commit/1b700a78ea6495bf6f3a692a84ee0685de02853f))
* **deps:** update plugin kotlin-qa to v0.14.0 ([a1102a3](https://github.com/DanySK/Alchemist-experiments-startup/commit/a1102a32e1f5d8b1b95fc2dedbea34e4408c1633))
* **deps:** update plugin kotlin-qa to v0.14.1 ([ebd110e](https://github.com/DanySK/Alchemist-experiments-startup/commit/ebd110e2b8cf59e7d447e8d0fba08ddf83a0a23c))
* **deps:** update plugin kotlin-qa to v0.14.2 ([b7a65a7](https://github.com/DanySK/Alchemist-experiments-startup/commit/b7a65a781351ded97da5368860e6511a8c990dff))
* **deps:** update plugin kotlin-qa to v0.15.0 ([cfe3149](https://github.com/DanySK/Alchemist-experiments-startup/commit/cfe31497e4371435638cdd09c4149e6480efacf7))
* **deps:** update plugin kotlin-qa to v0.15.1 ([ede2be3](https://github.com/DanySK/Alchemist-experiments-startup/commit/ede2be36f8f56f5928dd50175467ef2363592760))
* **deps:** update plugin kotlin-qa to v0.16.0 ([588dd5f](https://github.com/DanySK/Alchemist-experiments-startup/commit/588dd5fc0247989a0fa677eece61751ca72f9890))
* **deps:** update plugin kotlin-qa to v0.16.1 ([91ba758](https://github.com/DanySK/Alchemist-experiments-startup/commit/91ba7587e6b1895092e28258a660222e79d1c185))
* **deps:** update plugin kotlin-qa to v0.18.0 ([2db181e](https://github.com/DanySK/Alchemist-experiments-startup/commit/2db181ef56fa17d9016f0f8e7d6c07adebdca705))
* **deps:** update plugin kotlin-qa to v0.19.0 ([404a320](https://github.com/DanySK/Alchemist-experiments-startup/commit/404a32037ce4155419ea20cbc3e7749a35245508))
* **deps:** update plugin kotlin-qa to v0.19.1 ([accc86a](https://github.com/DanySK/Alchemist-experiments-startup/commit/accc86ae1aef39c8136db17aaa7609796c956c3a))
* **deps:** update plugin kotlin-qa to v0.20.3 ([20b6c3a](https://github.com/DanySK/Alchemist-experiments-startup/commit/20b6c3a70ba545d93e8ca1c20f23dec9d27e0060))
* **deps:** update plugin kotlin-qa to v0.20.4 ([7c80ac8](https://github.com/DanySK/Alchemist-experiments-startup/commit/7c80ac8a889a8eda61cb94dcd57875ed01e574a0))
* **deps:** update plugin kotlin-qa to v0.21.0 ([32ee127](https://github.com/DanySK/Alchemist-experiments-startup/commit/32ee127ffaae2c1795d7ebc83c3ad468529fad92))
* **deps:** update plugin kotlin-qa to v0.22.0 ([58b0895](https://github.com/DanySK/Alchemist-experiments-startup/commit/58b0895e6dd89f2c5be46b6f048bf43fc4a2c65d))
* **deps:** update plugin kotlin-qa to v0.22.1 ([80b81ae](https://github.com/DanySK/Alchemist-experiments-startup/commit/80b81ae42952d9b3fa9468ff02049c027c41e5ff))
* **deps:** update plugin kotlin-qa to v0.22.2 ([4eb7ca9](https://github.com/DanySK/Alchemist-experiments-startup/commit/4eb7ca953c1029cf8bbda6bc339307c9eea5ebe7))
* **deps:** update plugin kotlin-qa to v0.23.0 ([d8ad7ad](https://github.com/DanySK/Alchemist-experiments-startup/commit/d8ad7ad8b6b7734ceaafd5983c04de2ad0d1386d))
* **deps:** update plugin kotlin-qa to v0.23.1 ([a8d508a](https://github.com/DanySK/Alchemist-experiments-startup/commit/a8d508aff0cd04ec94d80f75b5916fc50fbe03bd))
* **deps:** update plugin kotlin-qa to v0.23.2 ([02d79e9](https://github.com/DanySK/Alchemist-experiments-startup/commit/02d79e986fb15aef33df920e6b517d6958f0da78))
* **deps:** update plugin kotlin-qa to v0.24.0 ([4e83b40](https://github.com/DanySK/Alchemist-experiments-startup/commit/4e83b40b12f49c366fc18a9301305498cf6caded))
* **deps:** update plugin kotlin-qa to v0.25.0 ([790e4a4](https://github.com/DanySK/Alchemist-experiments-startup/commit/790e4a4e32453fdb27aad7340d3b24b7028c5d5a))
* **deps:** update plugin kotlin-qa to v0.25.1 ([6fcd004](https://github.com/DanySK/Alchemist-experiments-startup/commit/6fcd004a27e8fa62cbd675694420987906c3b646))
* **deps:** update plugin kotlin-qa to v0.26.0 ([3f7147d](https://github.com/DanySK/Alchemist-experiments-startup/commit/3f7147dcc3845fc797bd1cce1d7fcccc59ed059c))
* **deps:** update plugin kotlin-qa to v0.26.1 ([6f3fb07](https://github.com/DanySK/Alchemist-experiments-startup/commit/6f3fb075a037bb201c85386c9aba8604207585fb))
* **deps:** update plugin kotlin-qa to v0.27.0 ([07ce777](https://github.com/DanySK/Alchemist-experiments-startup/commit/07ce77747b4c1b73a19afafc2130481ba0825976))
* **deps:** update plugin kotlin-qa to v0.27.1 ([4eba7e3](https://github.com/DanySK/Alchemist-experiments-startup/commit/4eba7e3277d0d93b96f9bb748a862ade29250781))
* **deps:** update plugin kotlin-qa to v0.28.0 ([52b6e27](https://github.com/DanySK/Alchemist-experiments-startup/commit/52b6e274164ac5f9723a146db4771667bcba2510))
* **deps:** update plugin kotlin-qa to v0.29.0 ([51f7ca3](https://github.com/DanySK/Alchemist-experiments-startup/commit/51f7ca385bc53abda5eb436d2a06a67635d97328))
* **deps:** update plugin kotlin-qa to v0.29.1 ([0f8edc6](https://github.com/DanySK/Alchemist-experiments-startup/commit/0f8edc62ab6664368f6992f6f0547ec3cdcc59cf))
* **deps:** update plugin kotlin-qa to v0.29.2 ([05bbfd7](https://github.com/DanySK/Alchemist-experiments-startup/commit/05bbfd7e4399dc12d3f76157927370e50ca8c93b))
* **deps:** update plugin kotlin-qa to v0.31.0 ([8cf8127](https://github.com/DanySK/Alchemist-experiments-startup/commit/8cf8127ec08544f7832921583f0f92103c694178))
* **deps:** update plugin kotlin-qa to v0.6.0 ([6be1e1e](https://github.com/DanySK/Alchemist-experiments-startup/commit/6be1e1e14e2616e31f752bed2c2bf69cfbc893b3))
* **deps:** update plugin kotlin-qa to v0.7.0 ([5ca5d1d](https://github.com/DanySK/Alchemist-experiments-startup/commit/5ca5d1d91c3e42631b2af5b0be33d9004ea03f8f))
* **deps:** update plugin kotlin-qa to v0.7.1 ([9319000](https://github.com/DanySK/Alchemist-experiments-startup/commit/9319000ac69b75c5e259216b7b5f57096f679512))
* **deps:** update plugin kotlin-qa to v0.8.0 ([b9c4870](https://github.com/DanySK/Alchemist-experiments-startup/commit/b9c4870dbc440b10c25bc0020fc979559c85ebb0))
* **deps:** update plugin kotlin-qa to v0.8.1 ([b81c36f](https://github.com/DanySK/Alchemist-experiments-startup/commit/b81c36f0f790f377babf8047dfab29d3fbd000df))
* **deps:** update plugin kotlin-qa to v0.8.2 ([e5f44f3](https://github.com/DanySK/Alchemist-experiments-startup/commit/e5f44f314560d0f8c9e3b674fc562260f764ca69))
* **deps:** update plugin kotlin-qa to v0.8.3 ([894f1f9](https://github.com/DanySK/Alchemist-experiments-startup/commit/894f1f97766f28c3913e8564070ea78488767e77))
* **deps:** update plugin kotlin-qa to v0.9.0 ([684ca18](https://github.com/DanySK/Alchemist-experiments-startup/commit/684ca18945fd2071c1e1bb1ef021e64d7f5c7a7e))
* **deps:** update plugin multijvmtesting to v0.2.0 ([42dee20](https://github.com/DanySK/Alchemist-experiments-startup/commit/42dee200a3100e1b7876daec1ed9cce6a910dbff))
* **deps:** update plugin multijvmtesting to v0.2.1 ([45964c5](https://github.com/DanySK/Alchemist-experiments-startup/commit/45964c568352c7f7425cc5a4e6ffc9f2513eda4e))
* **deps:** update plugin multijvmtesting to v0.2.2 ([e13d083](https://github.com/DanySK/Alchemist-experiments-startup/commit/e13d0838a202bf2732510b856b753983fcd6c441))
* **deps:** update plugin multijvmtesting to v0.3.0 ([74c8c3b](https://github.com/DanySK/Alchemist-experiments-startup/commit/74c8c3b7ae67e6ad33138d99ed7c194a72680334))
* **deps:** update plugin multijvmtesting to v0.3.1 ([ba70006](https://github.com/DanySK/Alchemist-experiments-startup/commit/ba70006cc17ae665725f72fe83b87a97ba1fadb3))
* **deps:** update plugin multijvmtesting to v0.3.2 ([d34d6ca](https://github.com/DanySK/Alchemist-experiments-startup/commit/d34d6ca93e56b25b729765a7b4195fa5b15e1e5a))
* **deps:** update plugin multijvmtesting to v0.3.3 ([847eee9](https://github.com/DanySK/Alchemist-experiments-startup/commit/847eee948f9c2dcfbaa224242ddc6fecbe16d7e0))
* **deps:** update plugin multijvmtesting to v0.3.4 ([6696eb9](https://github.com/DanySK/Alchemist-experiments-startup/commit/6696eb936cee87d3930cbd0dc1968156ee115148))
* **deps:** update plugin multijvmtesting to v0.3.5 ([9231d50](https://github.com/DanySK/Alchemist-experiments-startup/commit/9231d508b35b999c1bbee84b201fbb5f3a550c87))
* **deps:** update plugin multijvmtesting to v0.3.6 ([6f148e1](https://github.com/DanySK/Alchemist-experiments-startup/commit/6f148e10ffc0aa662d7bc089ea6cbd6f262ea07b))
* **deps:** update plugin multijvmtesting to v0.3.7 ([edfe125](https://github.com/DanySK/Alchemist-experiments-startup/commit/edfe1251670a8e5ae97fb21f0b6754c44fb7f2fe))
* **deps:** update plugin multijvmtesting to v0.4.0 ([019b8d6](https://github.com/DanySK/Alchemist-experiments-startup/commit/019b8d601893ff635a670e02c72db458ed4bf79e))
* **deps:** update plugin multijvmtesting to v0.4.10 ([5532ae5](https://github.com/DanySK/Alchemist-experiments-startup/commit/5532ae5ed538f7b109624f52a33bb91b4d59c2bb))
* **deps:** update plugin multijvmtesting to v0.4.11 ([5f9b2bd](https://github.com/DanySK/Alchemist-experiments-startup/commit/5f9b2bdb8b4e09a2b3452e4945fe4bc01feecfdb))
* **deps:** update plugin multijvmtesting to v0.4.12 ([2d85f9a](https://github.com/DanySK/Alchemist-experiments-startup/commit/2d85f9ad7033cb8304b30dca8f63bd3c5404ba2a))
* **deps:** update plugin multijvmtesting to v0.4.13 ([c02123a](https://github.com/DanySK/Alchemist-experiments-startup/commit/c02123ab6266c91491edf5f940096a2e01f7f750))
* **deps:** update plugin multijvmtesting to v0.4.14 ([2528431](https://github.com/DanySK/Alchemist-experiments-startup/commit/252843130a6685532fa6d2b9473d2c417f8d7a98))
* **deps:** update plugin multijvmtesting to v0.4.15 ([96fb9b5](https://github.com/DanySK/Alchemist-experiments-startup/commit/96fb9b53f689e129968c6fa79cfb189202d444ed))
* **deps:** update plugin multijvmtesting to v0.4.2 ([ba3a73a](https://github.com/DanySK/Alchemist-experiments-startup/commit/ba3a73a90b1ccdd86504c1e04c895c72d5c0ba3e))
* **deps:** update plugin multijvmtesting to v0.4.3 ([ef7d9b8](https://github.com/DanySK/Alchemist-experiments-startup/commit/ef7d9b85cb5cb10c50552f3c08249a2d8f887b47))
* **deps:** update plugin multijvmtesting to v0.4.4 ([9a84920](https://github.com/DanySK/Alchemist-experiments-startup/commit/9a849209036728d7e590cd3828f6d77bcc185879))
* **deps:** update plugin multijvmtesting to v0.4.5 ([3e8720b](https://github.com/DanySK/Alchemist-experiments-startup/commit/3e8720b6654bf692ce347d49c052a1448dd4c89a))
* **deps:** update plugin multijvmtesting to v0.4.6 ([168f727](https://github.com/DanySK/Alchemist-experiments-startup/commit/168f7272229926cb00cf369bea890135ad040f4b))
* **deps:** update plugin multijvmtesting to v0.4.7 ([0935925](https://github.com/DanySK/Alchemist-experiments-startup/commit/0935925bf1bb9577823753e87d6e4785641d9d6e))
* **deps:** update plugin multijvmtesting to v0.4.8 ([62c0918](https://github.com/DanySK/Alchemist-experiments-startup/commit/62c0918a4790a214eba1491acfa5b602777e0a12))
* **deps:** update plugin multijvmtesting to v0.4.9 ([14648ea](https://github.com/DanySK/Alchemist-experiments-startup/commit/14648eaf59eac187d7f8e91e850cd5a848e9a541))


### Build and continuous integration

* add missing checkout ([717cb24](https://github.com/DanySK/Alchemist-experiments-startup/commit/717cb240fc603f78e162bf8da310f47ba6714658))
* add pipeline summary job ([d7ed0ed](https://github.com/DanySK/Alchemist-experiments-startup/commit/d7ed0ed194ed307d6032a25136dcd67dd1d8088a))
* add the mergify config from Alchemist ([dc1905a](https://github.com/DanySK/Alchemist-experiments-startup/commit/dc1905a5ff8eb3d8f32bbb91699ef038312d9ff5))
* allow release updates in case of re-runs ([eb85b63](https://github.com/DanySK/Alchemist-experiments-startup/commit/eb85b633407d9cd28deb268ff28c405ae451e3b0))
* create .python-version ([34a9263](https://github.com/DanySK/Alchemist-experiments-startup/commit/34a926301656bcc9543e1353f9d4772608dacec0))
* **deps:** update actions/cache action to v3 ([9413833](https://github.com/DanySK/Alchemist-experiments-startup/commit/94138335d5a21ba48eeae9feac2d1f9e4372f3d9))
* **deps:** update actions/checkout action to v3.0.2 ([249cb0b](https://github.com/DanySK/Alchemist-experiments-startup/commit/249cb0bfea74e44d857f169ab6dac00c64534b62))
* **deps:** update actions/checkout action to v3.1.0 ([c7de7d2](https://github.com/DanySK/Alchemist-experiments-startup/commit/c7de7d2c691d9c3378407a3c2ceb556cd8b2dc45))
* **deps:** update actions/checkout action to v3.2.0 ([80f5c95](https://github.com/DanySK/Alchemist-experiments-startup/commit/80f5c952f28806839dd85a840cee187ff11fa1fd))
* **deps:** update actions/checkout action to v3.3.0 ([a2711e6](https://github.com/DanySK/Alchemist-experiments-startup/commit/a2711e6aa739a60aab291bb3d34eaa7e7237ae7b))
* **deps:** update actions/setup-python action to v3 ([a1bafd2](https://github.com/DanySK/Alchemist-experiments-startup/commit/a1bafd298800ff2977c3994ce1a39e10d38f3edc))
* **deps:** update danysk/action-checkout action to v0.2.1 ([9851f1a](https://github.com/DanySK/Alchemist-experiments-startup/commit/9851f1a9cef812c2c55d912668b5b1b1b23bc82d))
* **deps:** update danysk/action-checkout action to v0.2.2 ([212e6b3](https://github.com/DanySK/Alchemist-experiments-startup/commit/212e6b3889991b2b0dc556991c7fd6757f3d7e42))
* **deps:** update danysk/action-checkout action to v0.2.3 ([b1435e3](https://github.com/DanySK/Alchemist-experiments-startup/commit/b1435e32fb297f042a054f2e7989ee9fc878958f))
* **deps:** update danysk/action-checkout action to v0.2.4 ([c072c7d](https://github.com/DanySK/Alchemist-experiments-startup/commit/c072c7d5fb3fdceb2b47173d2b125ab285cb6601))
* **deps:** update danysk/action-checkout action to v0.2.5 ([66265ec](https://github.com/DanySK/Alchemist-experiments-startup/commit/66265ece7c2341a63941ca7f84bc9c38ac10bf56))
* **deps:** update danysk/build-check-deploy-gradle-action action to v1.2.15 ([4b12b50](https://github.com/DanySK/Alchemist-experiments-startup/commit/4b12b50ea93ad5444a3da8a1ebf34a683567a5c3))
* **deps:** update danysk/build-check-deploy-gradle-action action to v1.2.16 ([8c8ae77](https://github.com/DanySK/Alchemist-experiments-startup/commit/8c8ae773659b080bcb106b2647b8530d3dab3314))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2 ([c8db7aa](https://github.com/DanySK/Alchemist-experiments-startup/commit/c8db7aa052f5825a9d9c59de258d5ecd6a3c8f8a))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.0.1 ([d34c473](https://github.com/DanySK/Alchemist-experiments-startup/commit/d34c473463ef2664e29a7aa26032c12925e136f6))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.0.2 ([8c89e08](https://github.com/DanySK/Alchemist-experiments-startup/commit/8c89e08c1cab3daad604b678dbf7dd0c9da73a75))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.0.3 ([003595d](https://github.com/DanySK/Alchemist-experiments-startup/commit/003595d73f8dd0df24b0e36b1db93f738dc77c7c))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.0 ([4d83e97](https://github.com/DanySK/Alchemist-experiments-startup/commit/4d83e97f4da4670d3c3bcb905f882e806c1d814b))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.1 ([ebb39c1](https://github.com/DanySK/Alchemist-experiments-startup/commit/ebb39c1a23c56791de8ab16e3dac378497d659cd))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.10 ([f8eeb58](https://github.com/DanySK/Alchemist-experiments-startup/commit/f8eeb58179dda2cc76da3f8009fbe0a1e18a4a2e))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.11 ([1891808](https://github.com/DanySK/Alchemist-experiments-startup/commit/1891808d79c80965e79261692a0c702b34bfb970))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.12 ([60abb21](https://github.com/DanySK/Alchemist-experiments-startup/commit/60abb21d188e57f5a06cfc97ce0372f8443c2b48))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.13 ([26c174a](https://github.com/DanySK/Alchemist-experiments-startup/commit/26c174a3d7eb64f458eb8cbcf4e2ad1985e5b574))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.14 ([bb7ec31](https://github.com/DanySK/Alchemist-experiments-startup/commit/bb7ec31c6331611c697a5ac7e4d8129f65d67a5e))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.15 ([cd750a1](https://github.com/DanySK/Alchemist-experiments-startup/commit/cd750a116f08000dca16cbc3be56a03ade987a58))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.16 ([ce873e6](https://github.com/DanySK/Alchemist-experiments-startup/commit/ce873e61160ab150d7a91b24d66b65aafd9bd319))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.17 ([06227b0](https://github.com/DanySK/Alchemist-experiments-startup/commit/06227b0356812ca8cc10cf11aec48674e3975fa4))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.18 ([1c62c01](https://github.com/DanySK/Alchemist-experiments-startup/commit/1c62c01eee12cb3e9cbae41fa89c58fdf7fff98d))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.19 ([4bde933](https://github.com/DanySK/Alchemist-experiments-startup/commit/4bde933dd11e6af7fc28c71dade92db33e4abf5a))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.2 ([732c44f](https://github.com/DanySK/Alchemist-experiments-startup/commit/732c44f9d3779168a7df2884e5418ce144b84751))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.20 ([4556faa](https://github.com/DanySK/Alchemist-experiments-startup/commit/4556faab5b5e49f412de9c801fab3caa65145508))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.21 ([a201334](https://github.com/DanySK/Alchemist-experiments-startup/commit/a2013343d7942371add70856fc92d0a34c489ea1))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.3 ([ce5b522](https://github.com/DanySK/Alchemist-experiments-startup/commit/ce5b522750372a56c6e4f982582415c89c1d2afb))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.4 ([b2080f1](https://github.com/DanySK/Alchemist-experiments-startup/commit/b2080f176adec0d4d7e79ff045101ef15e283f33))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.5 ([3d31154](https://github.com/DanySK/Alchemist-experiments-startup/commit/3d311544a477889589ebe5330688189ca8069036))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.6 ([93d0390](https://github.com/DanySK/Alchemist-experiments-startup/commit/93d0390a85af99f841a917e808b3cc58bd3e7e7b))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.7 ([9a4496f](https://github.com/DanySK/Alchemist-experiments-startup/commit/9a4496ff104fd5d5e8b00e591726c5f17a047975))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.8 ([f14fe7d](https://github.com/DanySK/Alchemist-experiments-startup/commit/f14fe7dcdc6b6d6b8436f48c59bfec41c9759287))
* **deps:** update danysk/build-check-deploy-gradle-action action to v2.1.9 ([ff2ba6e](https://github.com/DanySK/Alchemist-experiments-startup/commit/ff2ba6ee3a284b65848faf6945daa32b43ded171))
* **deps:** update gabrielfalcao/pyenv-action action to v10 ([5d87ce8](https://github.com/DanySK/Alchemist-experiments-startup/commit/5d87ce8486e0245db464a4f6069827d7134abd1f))
* **deps:** update gabrielfalcao/pyenv-action action to v11 ([97a8ae6](https://github.com/DanySK/Alchemist-experiments-startup/commit/97a8ae6669f7bc7223cc30b882a8e94ea73ef3c7))
* **deps:** update ncipollo/release-action action to v1.10.0 ([8603573](https://github.com/DanySK/Alchemist-experiments-startup/commit/8603573b92d23dc87a0c8409406b59138c3a7385))
* **deps:** update ncipollo/release-action action to v1.10.1 ([906a6af](https://github.com/DanySK/Alchemist-experiments-startup/commit/906a6af4fa8fbad9f8b23251a451e6f5304c242d))
* **deps:** update ncipollo/release-action action to v1.11.0 ([483dd66](https://github.com/DanySK/Alchemist-experiments-startup/commit/483dd668ad497ab0070501d1611a9605a77089d1))
* **deps:** update ncipollo/release-action action to v1.11.1 ([e0633ce](https://github.com/DanySK/Alchemist-experiments-startup/commit/e0633ceb47fd45d56dcc86c238277e2c60935376))
* **deps:** update ncipollo/release-action action to v1.11.2 ([620a298](https://github.com/DanySK/Alchemist-experiments-startup/commit/620a298b321058038c5c3615b8507c01aac44f4f))
* **deps:** update ncipollo/release-action action to v1.12.0 ([45bd721](https://github.com/DanySK/Alchemist-experiments-startup/commit/45bd721c65861dd991d51cb1523b1d2d47cce8fe))
* disable codecov ([a25f6cf](https://github.com/DanySK/Alchemist-experiments-startup/commit/a25f6cfb25860945d3f86cd05da1caba50b386fe))
* lock the version of ncipollo/release-action ([c575905](https://github.com/DanySK/Alchemist-experiments-startup/commit/c5759051e6016a04477b178d088de58e672ba9ec))
* re-enable the multi-OS ([d866012](https://github.com/DanySK/Alchemist-experiments-startup/commit/d866012f5df216b874b38ed100605b4e891fb1bd))
* revamp the build ([15412b0](https://github.com/DanySK/Alchemist-experiments-startup/commit/15412b0f7342c441db3bb4b9f4f9563634a75030))
* switch to actions/setup-python ([52e6d41](https://github.com/DanySK/Alchemist-experiments-startup/commit/52e6d41699e3b7a691ba15f527817d2fe1109437))
* switch to pyenv ([b65d7dc](https://github.com/DanySK/Alchemist-experiments-startup/commit/b65d7dc3a57ec5be0f274ada921da0266be9928a))
* switch to the stable action for Gradle jobs ([9ceba67](https://github.com/DanySK/Alchemist-experiments-startup/commit/9ceba673a2ba1482bd2cce020c537907f425c1a6))
