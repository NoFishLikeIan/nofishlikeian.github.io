Accessibility notes
-------------------

This site received a set of small accessibility improvements:

- A "Skip to main content" link was added to the top of the page to assist keyboard users.
- The main content area now has id="content" and role="main" so assistive technologies can quickly jump to it.
- The primary navigation has role="navigation" and an aria-label. Current nav links use aria-current="page".
- A visually-hidden utility class and visible focus styles for the skip link were added to the inline CSS.
- Image alt text was reviewed and updated; please ensure all images in content include meaningful alt attributes.

Guidance for content editors
- Always add an `alt` attribute to images. If an image is decorative, use `alt=""`.
- Use headings (h1-h6) in logical order and avoid skipping heading levels where possible.
