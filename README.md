# English Fever – course content

Source material for courses on the English Fever WordPress site.
Learners are Latvian speakers; instructions and explanations are in Latvian, examples in English.

## Layout

```
courses/<level>/
  course.md              course outline, goals, unit list
  unit-NN/
    lesson.html          lesson page – paste into a WordPress page (Code editor / Custom HTML block)
    quiz.md              quiz questions (source for the H5P Question Set)
    slides.md            slide / video script
    h5p/*/content.json   H5P activity content (see tools/build_h5p.sh)
    downloads/           printable worksheets
```

## Workflow

1. Write or edit content here.
2. Build H5P packages: `tools/build_h5p.sh courses/b1/unit-01` creates `.h5p` files in `dist/`.
3. In WordPress: H5P Content > Add New > Upload, then embed the shortcode in the lesson page.
