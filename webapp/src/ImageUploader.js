import React, { useState } from "react"
import axios from "axios"

function ImageUploader() {
  const [selectedImage, setSelectedImage] = useState(null)

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    setSelectedImage(file)
  }

  const uploadImage = () => {
    if (selectedImage) {
      const formData = new FormData()
      formData.append("image", selectedImage)

      axios
        .post("http://localhost:3002/api/upload", formData) // Send the image to the server
        .then((response) => {
          console.log(
            "Image uploaded successfully. Server response:",
            response.data
          )
        })
        .catch((error) => {
          console.error("Error uploading image:", error)
        })
    }
  }

  return (
    <div>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={uploadImage}>Upload Image</button>
    </div>
  )
}

export default ImageUploader
