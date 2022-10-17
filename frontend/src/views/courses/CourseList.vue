<template>
    <div class="header py-16 flex flex-row justify-between dark:text-gray-400">
        <div>
            <h2 class="text-4xl font-bold">Courses</h2>
            <p class="text-sm">All courses are found here</p>
        </div>
        <div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
            </svg>

        </div>
    </div>

    <div class="grid grid-cols-2 gap-8">
        <figure class="md:flex bg-slate-100 rounded-sm p-8 md:p-0 dark:bg-slate-900">
            <img class="w-auto h-24 md:w-48 md:h-auto mx-auto" src="@/assets/images/course/1.jpg" alt="">
            <div class="pt-6 md:p-8 text-center md:text-left space-y-4">
                <h2 class="dark:text-gray-200 font-bold">Course Heading</h2>
                <blockquote>
                    <p class="text-sm font-normal dark:text-gray-600">
                        “Tailwind CSS is the only framework that I've seen scale
                        on large teams. It’s easy to customize, adapts to any design,
                        and the build size is tiny.”
                    </p>
                </blockquote>
                <figcaption class="font-medium">
                    <div class="text-sky-500 dark:text-sky-400">
                        Sarah Dayan
                    </div>
                    <div class="text-slate-700 dark:text-slate-500">
                        Staff Engineer, Algolia
                    </div>
                </figcaption>
            </div>
        </figure>

        <figure class="md:flex bg-slate-100 rounded-sm p-8 md:p-0 dark:bg-slate-900">
            <img class="w-auto h-24 md:w-48 md:h-auto mx-auto" src="@/assets/images/course/1.jpg" alt="">
            <div class="pt-6 md:p-8 text-center md:text-left space-y-4">
                <h2 class="dark:text-gray-200 font-bold">Course Heading</h2>
                <blockquote>
                    <p class="text-sm font-normal dark:text-gray-600">
                        “Tailwind CSS is the only framework that I've seen scale
                        on large teams. It’s easy to customize, adapts to any design,
                        and the build size is tiny.”
                    </p>
                </blockquote>
                <figcaption class="font-medium">
                    <div class="text-sky-500 dark:text-sky-400">
                        Sarah Dayan
                    </div>
                    <div class="text-slate-700 dark:text-slate-500">
                        Staff Engineer, Algolia
                    </div>
                </figcaption>
            </div>
        </figure>

    </div>
</template>