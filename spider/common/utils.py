import cairosvg
import ddddocr


def svg2png(image_bytes) -> int:
    img = cairosvg.svg2png(bytestring=image_bytes, background_color="#eee")

    ocr = ddddocr.DdddOcr(det=False, ocr=True, show_ad=False)

    res = ocr.classification(img)

    try:
        ret = eval(res)
        return ret
    except Exception:
        return svg2png(image_bytes)


if __name__ == '__main__':
    print(svg2png())
