# Parse Vision

Parse vision is an open source tool to visualise what OCR is parsing in a PDF document to help developers and product teams identify if the parsing has missed some vital information from the document.

## Why?

I was working on a proof of concept for an IDP platform (Intelligent Document Processing), and noticed that some information were missing from documents. So I decided to visualise the output to identify missing information quickly and validate which library would work better for different use cases.

Seeing many tutorials online claiming that parsing PDFs are easy, and adding LLMs on top to extract information, I decided to open source the tool to help developers and product teams making informed decisions about which library to use.

In the demo video, you'll notice that EasyOCR missed a quantity in the table, and Tesseract missed all the quantities.

## How to run

- Clone the repo.
- `pip install -r requirements.txt`
- `streamlit run index.py`

## Example

You can try the PDF example in the `example` folder.
Credit: [docmosis.com](https://resources.docmosis.com/example-templates/generate-multi-page-invoice-from-template)

## Demo Video

<video src="./demo.mp4"></video>

## Privacy

The tool runs locally, no data are sent outside your machine, no external logs, and no telemetry.

## OCR Libraries

- Tesseract
- EasyOCR

## Limitations & future work

- Configure the level of detection (blocks, lines, words).
- Configure using GPU or CPU.
- Add more libraries, such as PaddleOCR

## Connect

Feel free to connect with me on LinkedIn [Oras Al-Kubaisi](https://www.linkedin.com/in/oras-al-kubaisi/)
